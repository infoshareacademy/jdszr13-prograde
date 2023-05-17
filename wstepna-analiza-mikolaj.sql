--Całkowita wartość przewozu pasazerow i ladunku na linie lotnicze
select 
	"AIRLINE NAME" 
	, sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") total_passangers
from airlinewise_monthly_international_air_traffic amiat 
group by "AIRLINE NAME" 
order by total_passangers desc --pasazerowie

select 
	"AIRLINE NAME" 
	, sum("FREIGHT TO INDIA" + "FREIGHT FROM INDIA")::int total_freight_tonnes
from airlinewise_monthly_international_air_traffic amiat 
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
	from airlinewise_monthly_international_air_traffic amiat 
	group by "AIRLINE NAME"
) a -- wspolczynnik jest wysoki dodatni oznaczajacy wysoki poziom korelacji liniowej pomiedzy iloscia pasazerow i ladunku co wskazuje na niski poziom wyspecjalizowania w rodzaju przewozow

--najpopularniejsi przewoznicy to Jet Airways, Air India i Emirates Airlines
--------------------------

--najpopularniejszy cel podrozy wg ilosci pasazerow
select 
	city2 city
	, sum("PASSENGERS FROM CITY1 TO CITY2") passangers_to
from citypairwise_quarterly_international cqi 
group by city2
order by passangers_to desc --najpopularniejsze cele w indiach

select 
	city1 city
	, sum("PASSENGERS FROM CITY2 TO CITY1") passangers_to
from citypairwise_quarterly_international cqi 
group by city1 
order by passangers_to desc --najpopularniejsze cele zagraniczne

select sum("PASSENGERS FROM CITY1 TO CITY2") - sum("PASSENGERS FROM CITY2 TO CITY1") diff_domestic_foreign 
from citypairwise_quarterly_international cqi --2,295,487 wiecej pasazerow polecialo z miast indyjskich do miast zagranicznych niz z miast zagranicznych do indyjskich

select * from citypairwise_quarterly_international cqi 
order by "PASSENGERS FROM CITY1 TO CITY2" desc

select * from citypairwise_quarterly_international cqi 
order by "PASSENGERS FROM CITY2 TO CITY1"  desc

--zdecydowanie najpopularniejsze polaczenie wystepuje pomiedzy Dubai i Mumbai


---------------------------

select * from countrywise_quarterly_international_air_traffic cqiat 

select 
	"COUNTRY NAME" 
	, sum("PASSENGERS TO INDIA") passangers_to 
	, sum("PASSENGERS FROM INDIA") passangers_from
	, sum("FREIGHT TO INDIA")::int freight_to
	, sum("FREIGHT FROM INDIA")::int freight_from
from countrywise_quarterly_international_air_traffic cqiat 
group by "COUNTRY NAME" 
order by freight_from desc

--co bylo do przewidzenia najwiecej pasazerow przemieszcza sie do i z Zjednoczonych Emiratow Arabskich
--najwiecej ladunku z Indii zostalo wyslane do Hong Kongu i przyjete z ZEA