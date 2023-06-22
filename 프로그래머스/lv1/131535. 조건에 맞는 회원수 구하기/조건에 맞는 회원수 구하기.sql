-- 코드를 입력하세요
SELECT COUNT(USER_ID) AS USERS
from USER_INFO
where JOINED LIKE '2021-__-__' and age between 20 and 29