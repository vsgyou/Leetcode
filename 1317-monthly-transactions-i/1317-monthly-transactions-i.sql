# Write your MySQL query statement below
select date_format(trans_date, '%Y-%m') as month, 
        country, 
        count(*) as trans_count,
        count(case when state = 'approved' then id end) as approved_count, 
        sum(amount) as trans_total_amount, 
        ifnull(sum(case when state = 'approved' then amount end), 0) as approved_total_amount
from Transactions
group by month, country