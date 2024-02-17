-- The script lists all records of the table second_table having a name value in my MySQL server.
-- And records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
