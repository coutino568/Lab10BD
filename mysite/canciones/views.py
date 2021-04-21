from django.shortcuts import render
from .forms import CancionAddForm, AlbumAddForm, GeneroAddForm
from .models import Album, Cancion, Genero, Escuchar
from usuarios.models import Atributos_extra
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuarios.models import Suscripcion
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.db import IntegrityError

# Create your views here.

@login_required()
def cancion_add(request):
    userid = request.user.id
    if(Atributos_extra.objects.filter(usuario_id=userid).exists()):
        form = CancionAddForm(request.user)
        if request.method == 'POST':
            form = CancionAddForm(request.user, request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'canciones/add_cancion.html', context)
    else:
        return HttpResponseRedirect('../../canciones/list_cancion/')

@login_required()
def album_add(request):

    try:
        userid = request.user.id
        if(Atributos_extra.objects.filter(usuario_id=userid).exists()):
            form = AlbumAddForm()
            if request.method == 'POST':
                album_list = Album(username_usuario=request.user)
                form = AlbumAddForm(request.POST, instance=album_list)
                if form.is_valid():
                    form.save()
            context = {'form': form}
            return render(request, 'canciones/add_album.html', context)
        else:
            return HttpResponseRedirect('../../canciones/list_cancion/')

    except IntegrityError as e:
        form = AlbumAddForm()

        lista = ['Ese album ya existe']
        context = {'form': form, 'mensaje':lista}
        return render(request, "canciones/add_album.html", context)


@login_required()
def genero_add(request):
    form = GeneroAddForm()
    if request.method == 'POST':
        form =  GeneroAddForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'canciones/add_genero.html', context)

@login_required()
def cancion_list(request):
    all_canciones = Cancion.objects.all()
    all_albums = Album.objects.all()
    suscripcion = Suscripcion.objects.get(usuario=request.user)
    suscripcion_update = Suscripcion.objects.filter(usuario=request.user)
    cancion_reproducir = None
    if suscripcion.activa != True:
        if suscripcion.fecha_actualizacion < datetime.date.today():
            suscripcion_update.update(fecha_actualizacion = datetime.date.today() + datetime.timedelta(days=1))
            suscripcion_update.update(disponibilidad_de_reproducciones=3)
    if 'nombre' in request.GET:
        if request.GET['nombre'] != '':
            nombre_cancion = request.GET['nombre']
            all_canciones = all_canciones.filter(nombre = nombre_cancion)
    if 'album' in request.GET:
        if request.GET['album'] != '':
            nombre_album = request.GET['album']
            all_albums = all_albums.filter(titulo=nombre_album)
            all_canciones = all_canciones.filter(id_album__in=all_albums)
    if 'genero' in request.GET:
        if request.GET['genero'] != '':
            nombre_genero = request.GET['genero']
            all_generos = Genero.objects.all()
            all_generos = all_generos.filter(nombre=nombre_genero)
            all_albums = all_albums.filter(id_genero__in=all_generos)
            all_canciones = all_canciones.filter(id_album__in=all_albums)
    if 'artista' in request.GET:
        if request.GET['artista'] != '':
            nombre_artista = request.GET['artista']
            all_artistas = User.objects.all()
            all_artistas = all_artistas.filter(atributos_extra__nombre_artistico=nombre_artista)
            all_albums = all_albums.filter(username_usuario__in=all_artistas)
            all_canciones = all_canciones.filter(id_album__in=all_albums)
    if 'cancion_id' in request.POST:
        if request.POST['cancion_id'] != '' and  suscripcion != None:
            cancion_id = request.POST['cancion_id']
            cancion_id = int(cancion_id)
            cancion_reproducir = Cancion.objects.filter(id=cancion_id)
            if suscripcion.activa != True:
                if suscripcion.disponibilidad_de_reproducciones > 0:
                    suscripcion_update.update(disponibilidad_de_reproducciones=suscripcion.disponibilidad_de_reproducciones-1)
                    Escuchar.objects.create(username_usuario = request.user, id_cancion = Cancion.objects.get(id=cancion_id))
            else:
                Escuchar.objects.create(username_usuario = request.user, id_cancion = Cancion.objects.get(id=cancion_id))

    context = {
        'canciones': all_canciones,
        'reproducir': cancion_reproducir,
    }
    return render(request, 'canciones/canciones_list.html', context)
