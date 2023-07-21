-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, sum(b.SALES_AMOUNT * a.price) SALES
from PRODUCT a join OFFLINE_SALE b on a.PRODUCT_Id = b.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE asc