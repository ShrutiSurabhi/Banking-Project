/**** 17. Write a SQL query to find the country where the most assistant referees come from,
and the count of the assistant referees. ****/

SELECT COUNT(ass_ref_id) AS No_of_assistant_referees, country_name FROM asst_referee_mast ar
JOIN soccer_country sc
ON ar.country_id = sc.country_id
GROUP BY country_name
HAVING COUNT (ass_ref_id) = 
	(SELECT max(mm) FROM
		(SELECT COUNT(ass_ref_id) mm  FROM asst_referee_mast ar
         JOIN soccer_country sc
         ON ar.country_id = sc.country_id
         GROUP BY country_name)hh); 
