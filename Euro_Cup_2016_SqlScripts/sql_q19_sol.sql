/***** 19. Write a SQL query to find the number of captains who were also goalkeepers. *****/

SELECT COUNT(DISTINCT player_captain) no_of_captains FROM match_captain mc
JOIN player_mast pm 
ON mc.player_captain = pm.player_id 
WHERE posi_to_play = 'GK';