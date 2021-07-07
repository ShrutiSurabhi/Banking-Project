SELECT
	COUNT(CASE WHEN decided_by = 'P' THEN 1 END)
		FROM [euro_cup_2016].[dbo].[match_details]; 