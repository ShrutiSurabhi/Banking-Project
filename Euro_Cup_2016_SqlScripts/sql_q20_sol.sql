/***** 20.  Write a SQL query to find the substitute players who came into the field in the first
half of play, within a normal play schedule.****/

SELECT player_name, jersey_no, match_no FROM player_in_out pio
JOIN player_mast pm
ON pio.player_id = pm.player_id
WHERE play_half = '1'
AND in_out = 'I'
AND play_schedule = 'NT';
