select concat("YEAR",'-', "MONTH",'-01')::date year_month, SUM("PASSENGERS TO INDIA" +"PASSENGERS FROM INDIA") passangers from airlinewise_changed_date_format acdf
group by concat("YEAR",'-', "MONTH",'-01')::date
order by year_month