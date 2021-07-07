/***** 10. Write a SQL query to find all available information about the players under contract to
Liverpool F.C. playing for England in EURO Cup 2016. ****/

SELECT * FROM player_mast
WHERE playing_club = 'Liverpool'
AND team_id = (SELECT country_id FROM soccer_country WHERE country_name = 'ENGLAND');
