---------------pregunta 1 ----------
-----QUERRY que necesita hacer:
---(04 ES EL MES ; 2021 ES EL AñO)
select EXTRACT(year from fecha_reproduccion ) as year, EXTRACT(month from fecha_reproduccion ) as month,  g.nombre as genre, count(*) as cantidad_reproducciones from (
	select * from canciones_escuchar e
	join canciones_album a
	on e.id_cancion_id = a.id ) sub1
join canciones_genero g 
on  sub1.id_genero_id = g.id
where  EXTRACT(month from fecha_reproduccion ) = 04
and EXTRACT(year from fecha_reproduccion ) = 2021
group by month, year, genre



-----------------------
----Procedimiento :
create or replace function trends (mymonth varchar , myyear int)
	returns table 
	declare loweredmonth varchar
	begin
		if myyear>2022 or myyear < 2020 then
			raise exceotion 'Year is out of range';
		end if;
		loweredmonth = lower(mymonth)
		case loweredmonth
		when 'enero' then
			loweredmonth = '01';
		when 'febrero' then
			loweredmonth = '02';
		when 'marzo' then
			loweredmonth = '03';
		when 'abril' then
			loweredmonth = '04';
		when 'mayo' then
			loweredmonth = '05';
		when 'junio' then
			loweredmonth = '06';
		when 'julio' then
			loweredmonth = '07';
		when 'agosto' then
			loweredmonth = '08';
		when 'septiembre' then
			loweredmonth = '09';
		when 'octubre' then
			loweredmonth = '10';
		when 'noviembre' then
			loweredmonth = '11';
		when 'diciembre' then
			loweredmonth = '12';
		else
			raise esception 'Invalid Month';
		end case;





---------------------
---PREGUNTA 2

-----QUERY QUE NECESITA HACER:
--(01 ES EL ID DEL ALBUM ; 4 ES EL UMBRAL DE REPRODUCCIONES MINIMO)



select u.username as artista, a2.titulo as nombre_album, c.nombre as nombre_cancion, sub3.reproducciones from (
	select id_cancion_id , count (*) as reproducciones from(
		select * from (
			select * from canciones_escuchar e
			join canciones_cancion c
			on e.id_cancion_id = c.id 
			) sub1
		join canciones_album a
		on sub1.id_album_id = a.id
		where sub1.id_album_id = '01'
	
	) sub2
	group by id_cancion_id
) sub3
join canciones_cancion c
on c.id = sub3.id_cancion_id
join canciones_album a2
on a2.id = c.id_album_id
join auth_user u
on u.id = a2.username_usuario_id
where reproducciones > 4






---- PROCEDIMIENTO







---------------

----PREGUNTA 3

----QUERY

--- pt1  determina el nuemero de reproducciones que constituyen cierta posicion en el ranking
select distinct differentsongs from (
	select distinct u.username, count (*) as differentsongs from (
		select username_usuario_id as user , id_cancion_id as song, count (*)  from canciones_escuchar 
		group by id_cancion_id , username_usuario_id
		order by user ) sub1 
	join auth_user u
	on u.id = sub1.user
	group by u.username
) sub2
order by differentsongs desc
offset 2
limit 1

----pt 2  retorna los usuarios con una cantidad especifica de reproduccione
select * from (
	select distinct u.username, count (*) as differentsongs from (
		select username_usuario_id as user , id_cancion_id as song, count (*)  from canciones_escuchar 
		group by id_cancion_id , username_usuario_id
		order by user ) sub1 
	join auth_user u
	on u.id = sub1.user
	group by u.username
) sub2
where differentsongs = 3
order by differentsongs desc








-----PROCEDIMIENTO