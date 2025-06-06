# Write your MySQL query statement below
# LENGTH: 길이로 변환해주는 함수
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;