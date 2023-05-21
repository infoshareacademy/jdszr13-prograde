select sum("PASSENGERS FROM INDIA"), "MONTH"  from airlinewise_monthly_international_air_traffic_to_and_from_the_i amiattafti 
group by "MONTH"
order by sum("PASSENGERS FROM INDIA") DESC

select sum("PASSENGERS TO INDIA"), "MONTH"  from airlinewise_monthly_international_air_traffic_to_and_from_the_i amiattafti 
group by "MONTH"
order by sum("PASSENGERS TO INDIA") DESC

select sum("PASSENGERS TO INDIA") , "AIRLINE NAME"  from airlinewise_monthly_international_air_traffic_to_and_from_the_i amiattafti 
--where "AIRLINE NAME" = 'JET AIRWAYS' or "AIRLINE NAME" = 'AIR INDIA' or "AIRLINE NAME" = 'AIR INDIA EXPRESS'
group by "AIRLINE NAME"
order by sum("PASSENGERS TO INDIA") DESC