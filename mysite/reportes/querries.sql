
----pregunta 1
select * from canciones_album a 
join auth_user u 
on u.id = a.username_usuario_id 
where a.fecha_publicacion between current_date- interval '7 day' and current_date
order by fecha_publicacion desc , a.id desc
limit 5


-----pregunta 2




select t.id , t.nombre_artistico from (select u.id , ar.nombre_artistico, count(*) as reproducciones
from canciones_escuchar e 
join auth_user u 
on e.username_usuario_id=u.id 
join usuarios_atributos_extra ar 
on ar.usuario_id = u.id
where e.fecha_reproduccion between current_date - interval '3 months' and current_date - interval '1 months'
group by u.id, ar.nombre_artistico
order by count(*) desc) t
join
(select u.id , ar.nombre_artistico, count(*) as reproducciones
from canciones_escuchar e join auth_user u
on e.username_usuario_id=u.id join usuarios_atributos_extra ar 
on ar.usuario_id = u.id 
where e.fecha_reproduccion between current_date - interval '1 months' and current_date
group by u.id , ar.nombre_artistico
order by count(*) desc) r
on t.nombre_artistico = r.nombre_artistico
where t.reproducciones<r.reproducciones



-----------pregunta 3

select to_char(fecha_creacion , 'YYYY-MM') as fecha, count(*) as reproducciones 
from usuarios_suscripcion  s 
where fecha_creacion >= current_date - interval '3 months '  and fecha_creacion <= current_date 
and s.activa
group by fecha 
order by fecha desc




--pregunta 4
select u.id, u.username, sub1.canciones  from auth_user u 
join (
	select a.username_usuario_id as artista , count (*) as canciones from canciones_cancion c 
	join canciones_album a 
	on a.id = c.id_album_id
	group by artista 
	 
	limit 5
) sub1

on u.id = sub1.artista

order by sub1.canciones desc







----PREGUNTA 5
select g.nombre, count(*) from canciones_genero g
join canciones_album a
on g.id=a.id_genero_id 
join canciones_cancion c
on a.id=c.id_album_id join canciones_escuchar e on
c.id=e.id_cancion_id group by g.nombre order by count(*) desc limit 10




---PREGUNTA 6
select au.id, au.username , reproducciones from auth_user au 
join (	
	SELECT u.id , count (*) as reproducciones from canciones_escuchar e
	join auth_user u
	on u.id = e.username_usuario_id 
	group by u.id 
)sub1
on sub1.id = au.id 
order by reproducciones desc







