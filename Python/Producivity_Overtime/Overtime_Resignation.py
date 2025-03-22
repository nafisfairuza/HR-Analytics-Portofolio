import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_employee = pd.read_csv(r"Employee.csv")

#1. Factor Resign by Overtime
df_resign = df_employee[df_employee['Attrition'] == 'Yes']
overtime_resign = df_resign['OverTime'].value_counts(normalize=True) * 100 

plt.figure(figsize=(8, 5))
sns.barplot(x=overtime_resign.index, y=overtime_resign.values, palette=['blue', 'red'])
plt.title("Percentage of Resignation by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Resign (%)")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, val in enumerate(overtime_resign.values):
    plt.text(i, val + 1, f"{val:.2f}%", ha='center', fontsize=12)
plt.show()


#2. The Impact of Overtime on Employee Resignation: A Promotion Perspective
df_performancerating = pd.read_csv(r"C:\Users\THINKPAD\OneDrive\Documents\Dataset\HR_Analytics\PerformanceRating.csv")
df_merge = df_employee.merge(df_performancerating, on= 'EmployeeID', how= 'inner')

promotion_overtime = df_merge.groupby("OverTime")["YearsSinceLastPromotion"].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=promotion_overtime.index, y=promotion_overtime.values, palette=['blue', 'red'])
plt.title("The Impact of Overtime on Employee Resignation: A Promotion Perspective")
plt.xlabel("Overtime (Yes/No)")
plt.ylabel("Average Years Since Last Promotion")
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, val in enumerate(promotion_overtime.values):
    plt.text(i, val + 0.1, f"{val:.2f}", ha='center', fontsize=12)

plt.show()

#Insight
print(f"""
Based on the analysis, employees who frequently work overtime have a higher resignation rate.
This appears to be linked to the lack of promotion opportunities for those who work overtime,
which may be due to difficulties in managing time effectively or performance levels that are not considered sufficient for promotion.
In other words, excessive overtime could be an indicator that these employees are not receiving the same promotion opportunities as their colleagues who do not work overtime.
This highlights the need for greater attention to work-life balance in order to improve promotion prospects and reduce resignation rates.
""")
