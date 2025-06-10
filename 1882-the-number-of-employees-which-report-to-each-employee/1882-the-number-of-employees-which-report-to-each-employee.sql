# Write your MySQL query statement below
select e.employee_id, e.name, count(r.employee_id) as reports_count, round(avg(r.age), 0) as average_age
from Employees e
join Employees r
on e.employee_id = r.reports_to
group by e.employee_id, e.name
order by employee_id;
