-- Resignation Factors Based on Employee Overtime

SELECT 
    e.OverTime,  
    COUNT(CASE WHEN e.Attrition = 'Yes' THEN 1 END) AS Resigned_Employees,
    COUNT(*) AS Total_Employees,
    ROUND(100.0 * COUNT(CASE WHEN e.Attrition = 'Yes' THEN 1 END) / COUNT(*), 2) AS Turnover_Rate
FROM employee e 
GROUP BY e.OverTime
ORDER BY Turnover_Rate DESC;

-- Based on this data, employees who work overtime have a higher likelihood of resigning compared to those who do not.
