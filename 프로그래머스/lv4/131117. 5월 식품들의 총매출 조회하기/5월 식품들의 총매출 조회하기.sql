-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(p.price * o.amount) as TOTAL_SALES
from FOOD_PRODUCT as P join FOOD_ORDER as O on P.PRODUCT_ID = O.PRODUCT_ID
where PRODUCE_DATE like '%2022-05__%'
group by p.PRODUCT_ID 
order by TOTAL_SALES desc, p.PRODUCT_ID 