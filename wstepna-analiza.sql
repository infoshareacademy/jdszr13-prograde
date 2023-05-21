----------------------------------------------------------------------------------------------------------------------------------
--1) Najpopularniejszy kraj wybierany przez pasażerów lecących do Indii w okresie 2015Q1 to 2017Q1 w danym kwartale.
select c."COUNTRY NAME"  as indian_city,sum(c."PASSENGERS TO INDIA") as total_passengers_to_india, c."YEAR"::text as "YEAR",c.quarter as quarter 
from countrywise c
group by c."COUNTRY NAME", c."YEAR", c.quarter 
order by total_passengers_to_india desc; 
--Wynik: Najpopularniejszym krajem wybranym przez pasażerów lecących do Indii w okresie 2015Q1 to 2017Q1 w danym kwartale to  UNITED ARAB EMIRATES*


-- Najpopularniejszy kraj wybierany przez pasażerów lecących z Indii w okresie 2015Q1 to 2017Q1 w danym kwartale
select c."COUNTRY NAME"  as non_indian_city,sum(c."PASSENGERS FROM INDIA") as total_passengers_from_india, c."YEAR"::text as "YEAR",c.quarter as quarter 
from countrywise c
group by c."COUNTRY NAME" , c."YEAR" , c.quarter 
order by total_passengers_from_india desc; 
--Wynik: Najpopularniejszym krajem wybranym przez pasażerów lecących z Indii w okresie 2015Q1 to 2017Q1 w danym kwartale to  UNITED ARAB EMIRATES*

--Wspolczynnik korelacji pomiedzy liczbą pasazerow lecących do konkretnych krajów z pasażerów leciących do /walatujących z Indii
select 
corr(a.total_passengers_to_india,a.total_passengers_from_india)
from(
	select 
		 c."COUNTRY NAME" as "indian_city" , sum("PASSENGERS TO INDIA") as total_passengers_to_india
		, sum(c."PASSENGERS FROM INDIA") as total_passengers_from_india
		from countrywise c
		group by  c."COUNTRY NAME"
) a

--Wspolczynnik korelacji wynosi 0.9997169824754647, co oznacza bardzo silną korelację liniową pomiedzy wielkoscia przewozu pasazerow lecących oraz wylatujących z konkretnych państw Indii. Występująca tendencja wzrostowa obu badanych zmiennych, świadczy o występowaniu zależności pomiędzy nimi, uzależnienie przyjazdów do Indii oraz wylotów z UNITED ARAB EMIRATES.

-----------------------------------------------------------------------------------------------------------------------------------

--2. Główny typ przewoźnika (CARRIER TYPE) wraz z nazwą linni, liczbą lotów pasażerów do/z Indii oraz poziomem frachtu do/z Indii w okresie 2015Q1 to 2017Q1 w rozbiciu na kwartał.


select
	an."CARRIER TYPE",
	an."AIRLINE NAME",an."YEAR"::text,
	an.quarter guarter, 
	sum(an."PASSENGERS TO INDIA") passengers_to_india,
	sum(an."PASSENGERS FROM INDIA") passengers_from_india,
	sum(an."PASSENGERS TO INDIA" + an."PASSENGERS FROM INDIA") total_passengers,
	sum(an."FREIGHT TO INDIA")::int total_freight_to_india,
	sum(an."FREIGHT FROM INDIA")::int total_freight_from_india,
	sum(an."FREIGHT TO INDIA" + an."FREIGHT FROM INDIA")::int total_freight
from
	airlinewise an
group by
	"CARRIER TYPE",
	an."AIRLINE NAME",
	an."YEAR",
	an.quarter 
order by
	total_passengers desc,total_freight desc;
--Główny typ przewoźnika to krajowy, który przewiózł linią JET AIRWAYS najwięcej pasażerów ogółem,jak w podziale do/z Indii oraz przewiózł największą wartość frachtu w okresie 2015Q1 to 2017Q1 w danym kwartale.

-----------------------------------------------------------------------------------------------------------------------------------

--Całkowita wartość przewozu pasazerow i ladunku na linie lotnicze
select 
	"AIRLINE NAME" 
	, sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") total_passangers
from airlinewise a 
group by "AIRLINE NAME" 
order by total_passangers desc --pasazerowie

select 
	"AIRLINE NAME" 
	, sum("FREIGHT TO INDIA" + "FREIGHT FROM INDIA")::int total_freight_tonnes
from airlinewise a 
group by "AIRLINE NAME" 
order by total_freight_tonnes desc --ladunek

--Wspolczynnik korelacji pomiedzy wielkoscia przewozu pasazerow i ladunku
select 
corr(a.total_passangers, a.total_freight_tonnes)
from(
	select 
		"AIRLINE NAME" 
		, sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") total_passangers
		, sum("FREIGHT TO INDIA" + "FREIGHT FROM INDIA")::int total_freight_tonnes
	from airlinewise a 
	group by "AIRLINE NAME"
) a -- wspolczynnik jest wysoki dodatni oznaczajacy wysoki poziom korelacji liniowej pomiedzy iloscia pasazerow i ladunku co wskazuje na niski poziom wyspecjalizowania w rodzaju przewozow

--najpopularniejsi przewoznicy to Jet Airways, Air India i Emirates Airlines
--------------------------

--najpopularniejszy cel podrozy wg ilosci pasazerow
select 
	city2 city
	, sum("PASSENGERS FROM CITY1 TO CITY2") passangers_to
from citypairwise c 
group by city2
order by passangers_to desc --najpopularniejsze cele w indiach

select 
	city1 city
	, sum("PASSENGERS FROM CITY2 TO CITY1") passangers_to
from citypairwise c 
group by city1 
order by passangers_to desc --najpopularniejsze cele zagraniczne

select sum("PASSENGERS FROM CITY1 TO CITY2") - sum("PASSENGERS FROM CITY2 TO CITY1") diff_domestic_foreign 
from citypairwise c --2,295,487 wiecej pasazerow polecialo z miast indyjskich do miast zagranicznych niz z miast zagranicznych do indyjskich

select * from citypairwise c 
order by "PASSENGERS FROM CITY1 TO CITY2" desc

select * from citypairwise c 
order by "PASSENGERS FROM CITY2 TO CITY1"  desc

--zdecydowanie najpopularniejsze polaczenie wystepuje pomiedzy Dubai i Mumbai


---------------------------
select 
	"COUNTRY NAME" 
	, sum("PASSENGERS TO INDIA") passangers_to 
	, sum("PASSENGERS FROM INDIA") passangers_from
	, sum("FREIGHT TO INDIA")::int freight_to
	, sum("FREIGHT FROM INDIA")::int freight_from
from countrywise ct 
group by "COUNTRY NAME" 
order by freight_from desc

--co bylo do przewidzenia najwiecej pasazerow przemieszcza sie do i z Zjednoczonych Emiratow Arabskich
--najwiecej ladunku z Indii zostalo wyslane do Hong Kongu i przyjete z ZEA

----------------------------------------------------------------------------------------------------
select sum("PASSENGERS FROM INDIA"), "MONTH"  from airlinewise a 
group by "MONTH"
order by sum("PASSENGERS FROM INDIA") DESC

select sum("PASSENGERS TO INDIA"), "MONTH"  from airlinewise a 
group by "MONTH"
order by sum("PASSENGERS TO INDIA") DESC

select sum("PASSENGERS TO INDIA") , "AIRLINE NAME"  from airlinewise a 
--where "AIRLINE NAME" = 'JET AIRWAYS' or "AIRLINE NAME" = 'AIR INDIA' or "AIRLINE NAME" = 'AIR INDIA EXPRESS'
group by "AIRLINE NAME"
order by sum("PASSENGERS TO INDIA") desc
----------------------------------------------------------------------------------------------------

--porównanie wielkości udziału procentowego w przewozach pasażerskich w 
--kolejnych latach w zależności od przewoźnika


select  "AIRLINE NAME" ,"YEAR"::text , 
sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") Passengers,
round(sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA")::numeric /
(select sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA")
  from airlinewise a2 
  where "CARRIER TYPE" = 'DOMESTIC' and  "YEAR" = '2015')*100,2)share_Passengers
from airlinewise a 
where "CARRIER TYPE" = 'DOMESTIC' and  "YEAR" = '2015'
group by "AIRLINE NAME" ,"YEAR" 
union
select  "AIRLINE NAME" ,"YEAR"::text , 
sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") Passengers,
round(sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA")::numeric /
(select sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA")
  from airlinewise a2 
  where "CARRIER TYPE" = 'DOMESTIC' and  "YEAR" = '2016')*100,2) share_Passengers
from airlinewise a 
where "CARRIER TYPE" = 'DOMESTIC' and  "YEAR" = '2016'
group by "AIRLINE NAME" ,"YEAR" 
union
select  "AIRLINE NAME" ,"YEAR"::text , 
sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") Passengers,
round(sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA")::numeric /
(select sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA")
  from airlinewise a2 
  where "CARRIER TYPE" = 'DOMESTIC' and  "YEAR" = '2017')*100,2) share_Passengers
from airlinewise a 
where "CARRIER TYPE" = 'DOMESTIC' and  "YEAR" = '2017'
group by "AIRLINE NAME" ,"YEAR"  
order by "AIRLINE NAME", "YEAR" DESC
--duże firmy przewozowe tracą procentowy udział w rynku na rzecz małych
--przewoźników
