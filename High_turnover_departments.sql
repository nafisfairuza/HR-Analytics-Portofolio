-- High Turnover Departments

SELECT 
    e.Department,  
    COUNT(*) AS Total_Employees,
    COUNT(CASE WHEN e.Attrition = 'Yes' THEN 1 END) AS Resigned_Employees,
    ROUND(100.0 * COUNT(CASE WHEN e.Attrition = 'Yes' THEN 1 END) / COUNT(*), 2) AS Turnover_Rate
FROM employee e 
GROUP BY e.Department 
ORDER BY Turnover_Rate DESC;

-- Based on this data, the Sales department has a high turnover rate, with 92 resigned employees out of a total of 446
-- However, the Technology department has the highest number of resigned employees, with 133 out of a total of 961.
-- Although the Technology department has the highest number of resigned employees, its turnover rate might be lower compared to the Sales department due to a larger workforce.