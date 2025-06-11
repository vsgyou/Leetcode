# Write your MySQL query statement below
select round(count(a.player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from (select player_id, min(event_date) as first_login_date
from Activity
group by player_id) as firstlogin
join Activity a on firstlogin.player_id = a.player_id and a.event_date = date_add(firstlogin.first_login_date, interval 1 day)