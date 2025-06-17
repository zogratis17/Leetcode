select teacher_id ,count(distinct subject_id  )cnt
from Teacher 
group by 1