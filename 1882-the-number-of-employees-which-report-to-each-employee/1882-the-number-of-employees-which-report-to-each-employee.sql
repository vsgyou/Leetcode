# Write your MySQL query statement below
select e.employee_id, e.name, report.number as reports_count, report.aver_age as average_age
from Employees e
join (
    select reports_to, count(reports_to) as number, round(avg(age),0) as aver_age
    from Employees
    group by reports_to) as report
on (e.employee_id = report.reports_to)
order by e.employee_id