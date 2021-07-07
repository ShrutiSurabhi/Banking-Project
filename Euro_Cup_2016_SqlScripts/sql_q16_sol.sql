/****** 16. Write a SQL query to find referees and the number of matches they worked in each
venue. *****/

Select rm.referee_name, Count(mm.match_no) AS no_of_matches,sv.venue_name, sc.country_name FROM soccer_venue sv
JOIN  match_mast mm 
ON sv.venue_id = mm.venue_id
JOIN referee_mast rm
ON mm.referee_id = rm.referee_id
JOIN soccer_country sc
ON rm.country_id = sc.country_id
GROUP BY rm.referee_name,venue_name, country_name
ORDER BY referee_name; 