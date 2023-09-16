-- 코드를 입력하세요
SELECT i.NAME, i.DATETIME
from ANIMAL_INS as i
where i.animal_id not in (select animal_id from animal_outs)
order by DATETIME
limit 3

