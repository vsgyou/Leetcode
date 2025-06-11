# Write your MySQL query statement below
select round(count(A.player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from(
select player_id, min(event_date) as first_login_date
from Activity
group by player_id ) as firstlogin
join Activity A
on firstlogin.player_id = A.player_id
and A.event_date = date_add(firstlogin.first_login_date, interval 1 day);