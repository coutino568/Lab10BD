"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "playlists"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_playlist/', views.playlist_add, name='add_playlist'),
    path('add_esta_en/', views.esta_en_add, name='add_esta_en'),
    path('list_playlist/', views.playlist_list, name='list_playlist'),
    path('list_playlist/<int:playlist_id>/', views.cancion_list_playlist, name='list_playlist_canciones'),
]
