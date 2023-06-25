-- 코드를 입력하세요
SELECT CATEGORY, sum(SALES) AS TOTAL_SALES
from BOOK join BOOK_SALES using(book_id)
where SALES_DATE like '2022-01-__'
group by CATEGORY
order by CATEGORY