-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from FIRST_HALF as half join ICECREAM_INFO as info using(flavor)
group by ingredient_type