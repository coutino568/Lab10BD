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



