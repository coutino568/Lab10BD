from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum, Min, Max , Avg, Count
from canciones.models import Genero , Album ,Escuchar , Cancion
from usuarios.models import Atributos_extra, Suscripcion
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required(login_url='../../usuarios/login/')
def reportes(request):

	template = loader.get_template('reportes/reportes.html')
	context={}
	return HttpResponse(template.render(context, request))



@staff_member_required(login_url='../../usuarios/login/')
def reporte1(request):
	historial =Cancion.objects.raw('select * from canciones_album a join auth_user u on u.id = a.username_usuario_id where a.fecha_publicacion between current_date- interval \'7 days\' and current_date order by fecha_publicacion desc , a.id desc limit 5')
	template = loader.get_template('reportes/reporte1.html')
	context={'historial':historial}
	return HttpResponse(template.render(context, request))


@staff_member_required(login_url='../../usuarios/login/')
def reporte2(request):
	historial = Cancion.objects.raw('select t.id , t.nombre_artistico from (select u.id , ar.nombre_artistico, count(*) as reproducciones from canciones_escuchar e join auth_user u on e.username_usuario_id=u.id join usuarios_atributos_extra ar on ar.usuario_id = u.id where e.fecha_reproduccion between current_date - interval \'3 months\' and current_date - interval \'1 months\' group by u.id, ar.nombre_artistico order by count(*) desc) t join (select u.id , ar.nombre_artistico, count(*) as reproducciones from canciones_escuchar e join auth_user u on e.username_usuario_id=u.id join usuarios_atributos_extra ar on ar.usuario_id = u.id where e.fecha_reproduccion between current_date - interval \'1 months\' and current_date group by u.id , ar.nombre_artistico order by count(*) desc) r on t.nombre_artistico = r.nombre_artistico where t.reproducciones<r.reproducciones')
	template = loader.get_template('reportes/reporte2.html')
	context={'historial':historial}
	return HttpResponse(template.render(context, request))


@staff_member_required(login_url='../../usuarios/login/')
def reporte3(request):
	cursor = connection.cursor()
	cursor.execute('select to_char(fecha_creacion , \'YYYY-MM\') as fecha, count(*) as reproducciones from usuarios_suscripcion  s where fecha_creacion >= current_date - interval \'3 months \'  and fecha_creacion <= current_date and s.activa group by fecha order by fecha desc' )
	historial = cursor.fetchall()
	valores = []
	for elemento in historial:
		valores.append([elemento[0],elemento[1]])
	template = loader.get_template('reportes/reporte3.html')
	context={'valores': valores,}
	return HttpResponse(template.render(context, request))


@staff_member_required(login_url='../../usuarios/login/')
def reporte4(request):
	historial = Cancion.objects.raw('select u.id , u.username, sub1.canciones from auth_user u join (	select a.username_usuario_id as artista , count (*) as canciones from canciones_cancion c 	join canciones_album a 	on a.id = c.id_album_id	group by artista 		limit 5 ) sub1 on u.id = sub1.artista   order by canciones desc ' )
	template = loader.get_template('reportes/reporte4.html')
	context={'historial':historial}
	return HttpResponse(template.render(context, request))

@staff_member_required(login_url='../../usuarios/login/')
def reporte5(request):
	historial =Cancion.objects.raw('select g.id , g.nombre, count(*) as reproducciones from canciones_genero g join canciones_album a on g.id=a.id_genero_id join canciones_cancion c on a.id=c.id_album_id join canciones_escuchar e on c.id=e.id_cancion_id group by g.id , g.nombre order by reproducciones desc limit 10')
	template = loader.get_template('reportes/reporte5.html')
	context={'historial':historial}
	return HttpResponse(template.render(context, request))

@staff_member_required(login_url='../../usuarios/login/')
def reporte6(request):
	historial = User.objects.raw('select au.id, au.username , reproducciones from auth_user au join (		SELECT u.id , count (*) as reproducciones from canciones_escuchar e join auth_user u on u.id = e.username_usuario_id group by u.id )sub1 on sub1.id = au.id order by reproducciones desc')
	template = loader.get_template('reportes/reporte6.html')
	context={'historial': historial}
	return HttpResponse(template.render(context, request))
