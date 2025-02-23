--average of salary between employee with overtime and not

select 
	e.OverTime ,
	round(avg(e.Salary ),0) as average_salary
from employee e
group by e.OverTime
order by average_salary desc

-- Based on this data, employees who work overtime have a higher average salary. 
-- This is likely because they receive additional compensation for extra working hours compared to employees without overtime.
