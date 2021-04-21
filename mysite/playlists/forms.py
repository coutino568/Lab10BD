from django import forms
from .models import Playlist,Esta_en,Cancion

class PlaylistAddForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nombre']
        

class EstaEnAddForm(forms.ModelForm):
    class Meta:
        model = Esta_en
        fields = ['id_playlist','id_cancion']
    def __init__(self, user, *args, **kwrgs):
        super(EstaEnAddForm, self).__init__(*args, **kwrgs)
        if user:
            self.fields['id_playlist'].queryset = Playlist.objects.filter(username_usuario=user)

