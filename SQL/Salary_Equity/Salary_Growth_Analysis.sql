-- Salary Growth Analysis
SELECT 
    e.YearsAtCompany,
    ROUND(AVG(e.Salary), 0) AS avg_salary
FROM employee e
GROUP BY e.YearsAtCompany
ORDER BY e.YearsAtCompany;

-- Based on this data, employees with 5 years of experience tend to have lower salaries compared to those with fewer or more years of experience. 
-- His may indicate stagnation in career progression or differences in hiring salary trends over time.
