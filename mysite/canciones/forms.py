from django import forms
from .models import Cancion, Album, Genero

class CancionAddForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['nombre','id_album','fecha_publicacion','link']
    def __init__(self, user, *args, **kwrgs):
        super(CancionAddForm, self).__init__(*args, **kwrgs)
        if user:
            self.fields['id_album'].queryset = Album.objects.filter(username_usuario=user)
    
        
class AlbumAddForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo','id_genero','fecha_publicacion']

class GeneroAddForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

