-- Average of salary by jobrole

SELECT 
	e.JobRole, 
	ROUND(AVG(e.Salary), 0) AS average_salary
FROM employee e 
GROUP BY e.JobRole
ORDER BY average_salary desc;


-- Based on this data, the HR Manager has the highest salary among all job roles.
-- The Recruiter job role has the lowest salary in this dataset.
