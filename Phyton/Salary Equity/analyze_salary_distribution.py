import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"Employee.csv")

plt.style.use("ggplot")

plt.figure(figsize=(10, 6))

plt.hist(df['Salary'], bins=10, edgecolor='black', color='royalblue', alpha=0.8)

mean_salary = np.mean(df['Salary'])
plt.axvline(mean_salary, color="red", linestyle="dashed", linewidth=2, label=f'Mean Salary: {int(mean_salary)}')

plt.xlabel('Salary', fontsize=14)
plt.ylabel('Number of Employees', fontsize=14)
plt.title('Salary Distribution', fontsize=16, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

plt.xlabel("Salary\n\nInsight: Majority of employees earn below 100,000. Possible factors is job role, tenure.", fontsize=12, color="gray")

plt.tight_layout()
plt.show()

print(f"""
    From the histogram, we can observe that the salary distribution among employees is heavily skewed towards the lower salary range.
    A significant portion, around 753 employees, earn below 100,000, indicating a high concentration of lower-income employees.
    This trend could be influenced by several factors, such as job roles, tenure, or company pay structure.
    If most employees in this range are in entry-level positions, it may suggest that the organization has a large junior workforce.
    Alternatively, if senior positions are also concentrated in this lower salary range, it could indicate wage stagnation or limited salary growth opportunities.
    Further analysis, such as breaking down salaries by job roles or experience levels, would provide deeper insights into potential salary gaps and workforce distribution.
""")
