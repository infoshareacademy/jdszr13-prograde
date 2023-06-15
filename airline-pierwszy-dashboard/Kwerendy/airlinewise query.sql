select "AIRLINE NAME" , sum("PASSENGERS TO INDIA") passangers_arriving, sum("PASSENGERS FROM INDIA") passangers_departing, sum("PASSENGERS TO INDIA" + "PASSENGERS FROM INDIA") total from airlinewise a
group by "AIRLINE NAME" 
order by total desc