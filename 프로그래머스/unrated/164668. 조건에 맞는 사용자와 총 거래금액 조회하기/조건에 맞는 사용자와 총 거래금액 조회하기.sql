-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, SUM(PRICE) as TOTAL_SALES
from USED_GOODS_USER as u join USED_GOODS_BOARD as b on u.user_id = b.writer_id
where status = 'DONE'
group by u.user_id
having TOTAL_SALES >= 700000
order by TOTAL_SALES