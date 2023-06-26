-- 코드를 입력하세요
SELECT time_format(datetime, '%H') as hour, count(time_format(datetime, '%h')) as count
from animal_outs
where time_format(datetime, '%H') between 9 and 20 
group by hour
order by hour