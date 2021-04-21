from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, AuthenticationAddForm, AddAtributosExtraForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from .models import Suscripcion, Atributos_extra
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import datetime

def view_login(request):
    if request.user.is_authenticated != True:
        if request.method == "POST":
            form = AuthenticationAddForm(request.POST)

            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('../../canciones/list_cancion/')
        else:
            form = AuthenticationAddForm()
        context = {'form': form}
        return render(request, 'usuarios/login.html', context)
    else:
        return HttpResponseRedirect('../../canciones/list_cancion/')


def view_register(request):
    if request.user.is_authenticated != True:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = User.objects.create_user(**form.cleaned_data)
                Suscripcion.objects.create(usuario=new_user)
                return HttpResponseRedirect('../../canciones/list_cancion/')
        else:
            form = UserForm()
        context = {'form': form}
        return render(request, 'usuarios/register.html', context)
    else:
        return HttpResponseRedirect('../../canciones/list_cancion/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('../../usuarios/login/')

def perfil_view(request):
    return render(request, 'usuarios/perfil.html', {})

def suscribirme(request):
    #request.user.Suscripcion.objects.filter(activa=False).update(activa=True)
    userid = request.user.id
    #print(Suscripcion.objects.get(usuario_id=userid).activa)
    if(Suscripcion.objects.get(usuario_id=userid).activa == True):
        return HttpResponseRedirect('../../usuarios/perfil/')
    else:
        Suscripcion.objects.filter(usuario_id=userid).update(activa=True)
        Suscripcion.objects.filter(usuario_id=userid).update(fecha_creacion=datetime.date.today())
        return HttpResponseRedirect('../../usuarios/perfil/')

    context = {'activa': Suscripcion.objects.get(usuario_id=userid).activa}
    return render(request, 'usuarios/suscripcion.html', context)

def artista(request):
    if request.method == "POST":
        form = AddAtributosExtraForm(request.POST)
        userid = request.user.id
        if form.is_valid():
            Atributos_extra.objects.create(nombre_artistico = request.POST['nombre_artistico'], usuario_id=userid)
            return HttpResponseRedirect('../../usuarios/perfil/')
    else:
        form = AddAtributosExtraForm()
    context = {'form':form}
    return render(request, 'usuarios/artista.html', context)
