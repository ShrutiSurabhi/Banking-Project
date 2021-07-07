/******8. Write a SQL query to find the match number for the game with the highest number of
penalty shots, and which countries played that match.*****/

SELECT match_no, COUNT(*) shots FROM penalty_shootout
  GROUP BY match_no
  HAVING COUNT(*)= (SELECT MAX(shots)
                    FROM
					(SELECT COUNT(*) shots
					FROM penalty_shootout
					GROUP BY match_no) 
					inner_result);