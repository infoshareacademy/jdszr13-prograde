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