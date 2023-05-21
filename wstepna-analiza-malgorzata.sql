----------------------------------------------------------------------------------------------------------------------------------
select * from countrywise c;

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
	an."AIRLINE NAME", 
	sum(an."PASSENGERS TO INDIA") passengers_to_india,
	sum(an."PASSENGERS FROM INDIA") passengers_from_india,
	sum(an."PASSENGERS TO INDIA" + an."PASSENGERS FROM INDIA") total_passengers,
	sum(an."FREIGHT TO INDIA")::int total_freight_to_india,
	sum(an."FREIGHT FROM INDIA")::int total_freight_from_india,
	sum(an."FREIGHT TO INDIA" + an."FREIGHT FROM INDIA")::int total_freight,
	an."YEAR"::text,
	an.quarter guarter
from
	airlinewise_new an
group by
	"CARRIER TYPE",
	an."AIRLINE NAME",
	an."YEAR",
	an.quarter 
order by
	total_passengers desc,total_freight desc;


--Główny typ przewoźnika to krajowy, który przewiózł linią JET AIRWAYS najwięcej pasażerów ogółem,jak w podziale do/z Indii oraz przewiózł największą wartość frachtu w okresie 2015Q1 to 2017Q1 w danym kwartale.












