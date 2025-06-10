# Write your MySQL query statement below
# LENGTH: 길이로 변환해주는 함수
select tweet_id
from Tweets
where length(content) > 15