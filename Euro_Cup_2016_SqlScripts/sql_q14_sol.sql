/***** 14. Write a SQL query to find referees and the number of bookings they made for the
entire tournament. Sort your answer by the number of bookings in descending order ****/

SELECT referee_id,COUNT(*) as Bookings
 FROM player_booked pb
 JOIN match_mast mm 
 ON pb.match_no = mm.match_no 
 GROUP BY referee_id 
 ORDER BY COUNT(*) DESC;