-- Are employees who work overtime more likely to resign?

SELECT 
    e.OverTime,  
    round((COUNT(CASE WHEN e.Attrition = 'Yes' THEN 1 END)) * 100.0 / COUNT(*),1) AS percent_resigned
FROM employee e  
GROUP BY e.OverTime;

-- Based on this data, Reveals that employees who work overtime have a higher resignation rate despite higher satisfaction.
