import os, django, random
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
django.setup()


from faker import Faker
from canciones.models import Genero

genresList = ['Rock','Hip Hop','Jazz','Pop Music','Folk Music','Blues','Country Music',
'Musical Theatre',' Heavy Metal','Rhythm and Blues','Punk Rock','Classical Music',
'Soul Music','Reggae','House Music','Singing',
'Funk','Disco','Techno','Electronic Dance Music','Electronic Music','Ambient Music',
'Instrumental','Alternative Rock','Trance Music','Gospel Music',
'Dance Music','Popular Music','Swing Music','Drum and Bass','Electro','Psychedelic Music',
'Dubstep','Industrial Music','Orchestra','Hardcore','Opera','Progressive Rock','Breakbeat','Dub',
'Experimental Music','Synth-pop',
'Ska','World','Indie Rock','Baroque Music','Grunge','Pop Rock','Music of Africa','Reggaeton','Bachatai','Cumbia',
]






def createGenres () :
	for x in genresList :
		myName= x
		print(x)
		Genero.objects.create(nombre=myName)
		print( "-New genre created")


createGenres()

