/*****7. Write a SQL query to find all the venues where matches with penalty shootouts were
played.******/

SELECT venue_name FROM soccer_venue
     WHERE venue_id IN
       (SELECT venue_id
        FROM match_mast
        WHERE match_no IN
         (SELECT DISTINCT match_no
          FROM penalty_shootout));