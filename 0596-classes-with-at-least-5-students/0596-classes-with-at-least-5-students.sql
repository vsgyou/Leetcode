# Write your MySQL query statement below
select class
from (select class, count(student) as stu from Courses group by class) as aa
where stu >= 5

-- select class
-- from Courses
-- group by class
-- having count(student) >= 5;