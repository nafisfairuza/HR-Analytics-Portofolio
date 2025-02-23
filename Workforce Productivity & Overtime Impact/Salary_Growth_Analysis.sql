-- Difference in Employee Satisfaction Between Those Who Work Overtime and Those Who Do Not

SELECT 
    e.OverTime,
    round((COUNT(CASE WHEN s.SatisfactionID in (1,2) THEN 1 END) * 100.0 / COUNT(*)),1) AS percent_negatif_impact,
    round((COUNT(CASE WHEN s.SatisfactionID = 3 THEN 1 END) * 100.0 / COUNT(*)),1) AS percent_neutral,
    round((COUNT(CASE WHEN s.SatisfactionID in (4,5) THEN 1 END) * 100.0 / COUNT(*)),1) AS percent_positif_impact
FROM employee e
JOIN performancerating p ON e.EmployeeID = p.EmployeeID 
JOIN satisfiedlevel s ON p.JobSatisfaction = s.SatisfactionID
GROUP BY e.OverTime;

-- Based on this data, employees who work overtime tend to be more satisfied and experience a more positive impact.
-- This is likely because they receive additional compensation for extra working hours compared to employees who do not work overtime.