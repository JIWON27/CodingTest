-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, '%Y-%m-%d') START_DATE , DATE_FORMAT(END_DATE, '%Y-%m-%d') END_DATE, if ( datediff(END_DATE, START_DATE) + 1 >= 30, '장기 대여', '단기 대여') RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE like '%2022-09-__%'
order by HISTORY_ID desc