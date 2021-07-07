/**** 12. Write a SQL query that returns the total number of goals scored by each position on
each country’s team. Do not include positions which scored no goals *****/

SELECT player_name,posi_to_play,count(*) AS goals,country_name
FROM goal_details gd
JOIN player_mast pm ON gd.player_id=pm.player_id
JOIN soccer_country sc ON gd.team_id=sc.country_id
WHERE goal_schedule = 'NT'
GROUP BY player_name,posi_to_play,country_name
ORDER BY count(*);







