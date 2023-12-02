-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where lower(NAME) like lower('%EL%') and ANIMAL_TYPE = 'dog'
order by NAME