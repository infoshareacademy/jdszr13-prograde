----------------------------------------------------------------------------------------------------------------------------------
--Utworzenie nowych tabel airlinewise_new, citypairwise_new, countrywise_new  w celu dodania id serial jako primary key
--select * into airlinewise_new from airlinewise;
--select * into citypairwise_new from citypairwise c;
--select * into countrywise_new from countrywise c;

-- Do każdej z tabel dodano kolumnę id serial jako primary key
-- alter table airlinewise_new 
-- add id serial not null primary key;

-- alter table citypairwise_new 
-- add id serial not null primary key;

-- alter table countrywise_new 
-- add id serial not null primary key;

--1) Najpopularniejsze miasta wybierane przez pasażerów lecących do Indii oraz najpopularniejsze miasta zagraniczne wybierane przez pasażerów wylatujących z Indii w okresie 2015Q1 to 2017Q1.

-- Całkowita liczba pasażerów lecących do konkrytnych miast Indii
select cn.city2 as indian_city,sum(an."PASSENGERS TO INDIA") as total_passengers_to_india
from citypairwise_new cn 
join airlinewise_new an on cn.id = an.id
group by cn.city2 
order by total_passengers_to_india desc; 

-- Całkowita liczba pasażerów wylatujących za granicę
select cn.city1 as non_indian_city,sum(an."PASSENGERS FROM INDIA") as total_passengers_from_india
from citypairwise_new cn 
join airlinewise_new an on cn.id = an.id
group by cn.city1 
order by total_passengers_from_india desc; 


--Wspolczynnik korelacji pomiedzy liczbą pasazerow lecących do konkretnych miast Indii i wylatujących za granicę 
select 
corr(a.total_passengers_to_india,a.total_passengers_from_india)
from(
	select 
		 cn.city2 as "indian_city" , sum("PASSENGERS TO INDIA") as total_passengers_to_india
		, cn.city1 as "non_indian_city"
		, sum(an."PASSENGERS FROM INDIA") as total_passengers_from_india
		from citypairwise_new cn
		join airlinewise_new an on cn.id = an.id
	group by cn.city2, cn.city1 
) a

--Wspolczynnik korelacji wynosi 0.9870925562759706, co oznacza bardzo silną korelację liniową pomiedzy wielkoscia przewozu pasazerow lecących do konkretnych miast Indii i wylatujących za granicę. Występująca tendencja wzrostowa obu badanych zmiennych, świadczy o występowaniu zależności pomiędzy nimi, uzależnienie przyjazdów do miast Indii od wylotów do miast za granicą.

-----------------------------------------------------------------------------------------------------------------------------------

--2. Czy istnieje związek pomiędzy nazwą linii lotniczej (AIRLINE NAME) oraz typem przewoźnika (CARRIER TYPE), a liczbą lotów pasażerów do/z Indii oraz poziomem frachtu do/z Indii w okresie 2015Q1 to 2017Q1.

select
	"AIRLINE NAME",
	"CARRIER TYPE",
	sum(an."PASSENGERS TO INDIA") passengers_to_india,
	sum(an."PASSENGERS FROM INDIA") passengers_from_india,
	sum(an."PASSENGERS TO INDIA" + an."PASSENGERS FROM INDIA") total_passengers,
	sum(an."FREIGHT TO INDIA")::int total_freight_to_india,
	sum(an."FREIGHT FROM INDIA")::int total_freight_from_india,
	sum(an."FREIGHT TO INDIA" + an."FREIGHT FROM INDIA")::int total_freight,
	cn."COUNTRY NAME",
	an."YEAR"
from
	airlinewise_new an
join countrywise_new cn on
	an.id = cn.id
group by
	"AIRLINE NAME",
	"CARRIER TYPE",
	cn."COUNTRY NAME",
	an."YEAR"
order by
	total_passengers desc,total_freight desc;


--Istnieje związek pomiędzy nazwą linii lotniczej (AIRLINE NAME) oraz typem przewoźnika (CARRIER TYPE) a liczbą lotów pasażerów do/z Indii oraz poziomem frachtu do/z Indii. Największy ruch lotów przewozów pasażerów oraz frachtu obdywa się na linni zagraicznego przewoźnika EMIRATES AIRLINE.














