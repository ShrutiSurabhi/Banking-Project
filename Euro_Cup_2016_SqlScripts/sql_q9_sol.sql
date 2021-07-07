/**** 9. Write a SQL query to find the goalkeeper’s name and jersey number, playing for
Germany, who played in Germany’s group stage matches. ****/

SELECT player_name, jersey_no FROM player_mast WHERE player_id
 IN(SELECT player_gk  FROM match_details WHERE
		team_id = (SELECT country_id  FROM soccer_country
        WHERE country_name = 'Germany') 
		AND play_stage = 'G' )
	AND posi_to_play = 'GK';

		
		