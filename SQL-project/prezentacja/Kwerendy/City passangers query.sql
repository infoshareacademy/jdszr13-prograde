select city2 , sum("PASSENGERS FROM CITY1 TO CITY2") arrivals, sum("PASSENGERS FROM CITY2 TO CITY1") departures, sum("PASSENGERS FROM CITY1 TO CITY2" + "PASSENGERS FROM CITY2 TO CITY1") total from citypairwise c
group by city2 
union
select city1, sum("PASSENGERS FROM CITY1 TO CITY2") departures, sum("PASSENGERS FROM CITY2 TO CITY1") arrivals, sum("PASSENGERS FROM CITY1 TO CITY2" + "PASSENGERS FROM CITY2 TO CITY1") total from citypairwise c2 
group by city1
order by total desc