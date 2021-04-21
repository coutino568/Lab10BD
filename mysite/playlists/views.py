from django.shortcuts import render, get_object_or_404
from .forms import PlaylistAddForm, EstaEnAddForm
from .models import Playlist, Cancion, Esta_en
from canciones.models import Album, Escuchar
from usuarios.models import Suscripcion
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

# Create your views here.
@login_required()
def playlist_add(request):
    try:
        userid = request.user.id
        if(Suscripcion.objects.get(usuario_id=userid).activa == True):
            form = PlaylistAddForm()
            if request.method == 'POST':
                play_list = Playlist(username_usuario=request.user)
                form = PlaylistAddForm(request.POST, instance=play_list)
                if form.is_valid():
                    form.save()
            context = {'form': form}
            return render(request, 'playlists/add_playlist.html', context)
        else:
            return HttpResponseRedirect('../../canciones/list_cancion/')
    except IntegrityError as e:
        form = PlaylistAddForm()

        lista = ['Esta playlist ya existe']
        context = {'form': form, 'mensaje':lista}
        return render(request, "playlists/add_playlist.html", context)

@login_required()
def playlist_list(request):
    userid = request.user.id
    if(Suscripcion.objects.get(usuario_id=userid).activa == True):
        all_playlists_user = Playlist.objects.all()
        all_playlists_user = all_playlists_user.filter(username_usuario=request.user)
        context = {
            'playlists': all_playlists_user
        }
        return render(request, 'playlists/playlists_list.html', context)
    else:
        return HttpResponseRedirect('../../canciones/list_cancion/')

@login_required()
def esta_en_add(request):
    userid = request.user.id
    if(Suscripcion.objects.get(usuario_id=userid).activa == True):
        form = EstaEnAddForm(request.user)
        if request.method == 'POST':
            play_list = Playlist(request.user)
            form = EstaEnAddForm(request.user, request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'playlists/add_esta_en.html', context)
    else:
        return HttpResponseRedirect('../../canciones/list_cancion/')

@login_required()
def cancion_list_playlist(request, playlist_id):
    playlist_unica = get_object_or_404(Playlist, pk=playlist_id)
    if playlist_unica.username_usuario != request.user:
        return HttpResponseRedirect('../../list_playlist/')
    all_canciones = Cancion.objects.all()
    all_canciones = all_canciones.filter(esta_en__id_playlist=playlist_unica)
    all_albums = Album.objects.all()
    suscripcion = Suscripcion.objects.get(usuario=request.user)
    if suscripcion.activa == False:
        return HttpResponseRedirect('../../canciones/list_cancion/')
    suscripcion_update = Suscripcion.objects.filter(usuario=request.user)
    cancion_reproducir = None
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
            Escuchar.objects.create(username_usuario = request.user, id_cancion = Cancion.objects.get(id=cancion_id))
    context = {
        'canciones': all_canciones,
        'reproducir': cancion_reproducir,
    }
    return render(request, 'canciones/canciones_list.html', context)
