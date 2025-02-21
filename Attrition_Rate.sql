-- Attrition Rate

SELECT 
    ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS Resignation_Percentage
FROM employee

-- Based on this data, the attrition rate of employees who have resigned is 16.12% of the total workforce,
-- which suggests potential issues in employee retention.
-- Further analysis may be needed to identify specific reasons behind the high attrition rate and potential strategies to improve retention.