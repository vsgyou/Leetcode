# Write your MySQL query statement below
select s.user_id, round(case when count(c.user_id) = 0 then 0 else sum(c.action = 'confirmed') / count(c.user_id) end, 2) as confirmation_rate
from Signups s
left join Confirmations c on s.user_id = c.user_id
group by s.user_id