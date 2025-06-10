# Write your MySQL query statement below
DELETE P
FROM Person P
JOIN (
    SELECT MIN(id) AS min_id, email
    FROM Person
    GROUP BY email
) AS KeepRows
ON P.email = KeepRows.email AND P.id > KeepRows.min_id;