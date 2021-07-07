/***** 15. Write a SQL query to find the referees who booked the most number of players.
*****/
 
SELECT rm.referee_name,
       count(mm.match_no)
FROM player_booked pb
JOIN match_mast mm ON pb.match_no=mm.match_no
JOIN referee_mast rm ON mm.referee_id=rm.referee_id
GROUP BY referee_name
HAVING count(mm.match_no)=
  (SELECT max(mm)
   FROM
     (SELECT count(mm.match_no) mm
      FROM player_booked pb
      JOIN match_mast mm ON pb.match_no=mm.match_no
      JOIN referee_mast rm ON mm.referee_id=rm.referee_id
      GROUP BY referee_name) hh);