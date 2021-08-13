use springboardopt;
SET @v1 = 1612521;
SET @v2 = 1145072;
SET @v3 = 1828467;
SET @v4 = 'MGT382';
SET @v5 = 'Amber Hill';
SET @v6 = 'MGT';
SET @v7 = 'EE';			  
SET @v8 = 'MAT';


-- 1. List the name of the student with id equal to v1 (id).
EXPLAIN ANALYZE
SELECT name FROM Student WHERE id = @v1;

/*
-> Filter: (student.id = <cache>((@v1)))  (cost=41.00 rows=40) (actual time=0.927..0.927 rows=0 loops=1)
     -> Table scan on Student  (cost=41.00 rows=400) (actual time=0.048..0.225 rows=400 loops=1)
 
*/

/*
The query using full table scan that is slow. 
The reason is the original table doesn't have any index.
Solution: create primary index on uid
*/
ALTER TABLE Student ADD PRIMARY KEY (id);
EXPLAIN analyze
SELECT Student.name FROM Student WHERE id = @v1;
/*
-> Rows fetched before execution  (actual time=0.000..0.000 rows=1 loops=1)
*/

