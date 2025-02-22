-- Salary Gap by Education Level 
SELECT 
	e.Education,
	el.EducationLevel,
    ROUND(AVG(e.Salary), 0) AS average_salary
FROM employee e
JOIN educationlevel el ON e.Education = el.educationlevelID
GROUP BY e.Education, el.EducationLevel
ORDER BY el.educationlevelID

-- Based on this data, employees with higher education tend to have higher salaries compared to those with lower education levels.