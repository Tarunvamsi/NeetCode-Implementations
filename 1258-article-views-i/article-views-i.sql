# Write your MySQL query statement below
SELECT distinct author_id as id
FROM VIEWS
WHERE author_id = viewer_id
ORDER BY id asc;