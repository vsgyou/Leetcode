# Write your MySQL query statement below
select w2.id
from Weather w1
right join Weather w2 on w1.recordDate = date_sub(w2.recordDate, interval 1 day)
where w1.temperature < w2.temperature