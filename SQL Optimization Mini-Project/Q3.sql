DROP INDEX `PRIMARY` ON Student;

-- 3. List the names of students who have taken course v4 (crsCode).
EXPLAIN ANALYZE
SELECT name FROM Student WHERE id IN (SELECT studId FROM Transcript WHERE crsCode = @v4);
/*
-> Inner hash join (student.id = `<subquery2>`.studId)  (actual time=0.171..0.331 rows=2 loops=1)
     -> Table scan on Student  (cost=5.04 rows=400) (actual time=0.007..0.175 rows=400 loops=1)
     -> Hash
         -> Table scan on <subquery2>  (actual time=0.000..0.001 rows=2 loops=1)
             -> Materialize with deduplication  (actual time=0.094..0.094 rows=2 loops=1)
                 -> Filter: (transcript.studId is not null)  (cost=10.25 rows=10) (actual time=0.050..0.087 rows=2 loops=1)
                     -> Filter: (transcript.crsCode = <cache>((@v4)))  (cost=10.25 rows=10) (actual time=0.049..0.086 rows=2 loops=1)
                         -> Table scan on Transcript  (cost=10.25 rows=100) (actual time=0.030..0.071 rows=100 loops=1)
 
*/
EXPLAIN ANALYZE
SELECT name
FROM Student INNER JOIN Transcript ON Student.id = Transcript.studId
WHERE Transcript.crsCode = @v4;
/*
-> Inner hash join (student.id = transcript.studId)  (cost=411.29 rows=400) (actual time=0.139..0.280 rows=2 loops=1)
     -> Table scan on Student  (cost=0.50 rows=400) (actual time=0.005..0.161 rows=400 loops=1)
     -> Hash
         -> Filter: (transcript.crsCode = <cache>((@v4)))  (cost=10.25 rows=10) (actual time=0.035..0.069 rows=2 loops=1)
             -> Table scan on Transcript  (cost=10.25 rows=100) (actual time=0.018..0.055 rows=100 loops=1)
*/
