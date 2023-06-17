select "COUNTRY NAME" , sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") passangers_total, sum("PASSENGERS TO INDIA") passangers_to, sum("PASSENGERS FROM INDIA") passangers_from from countrywise c
group by "COUNTRY NAME" 
order by passangers_total DESC