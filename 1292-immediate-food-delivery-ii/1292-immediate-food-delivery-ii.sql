# Write your MySQL query statement below
select round(100*sum(order_date = customer_pref_delivery_date) / count(*), 2) as immediate_percentage 
from (
    select customer_id, order_date, customer_pref_delivery_date
    from Delivery
    where (customer_id, order_date) in (select customer_id, min(order_date)
                                        from Delivery
                                        group by customer_id)
                                        )
    as first_order
