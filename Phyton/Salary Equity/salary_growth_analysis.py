import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"Employee.csv")

df['Year'] = pd.to_datetime(df['HireDate']).dt.year

salary_trend = df.groupby('Year')['Salary'].mean()

plt.figure(figsize=(10, 6))
plt.plot(salary_trend.index, salary_trend.values, marker='o', linestyle='-', color='royalblue', label='Average Salary')
plt.axhline(y=salary_trend.mean(), color='red', linestyle='dashed', linewidth=2, label='Overall Average Salary')

plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Salary', fontsize=14)
plt.title('Salary Growth Analysis', fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.xlabel("Year\n\nInsight: Salary growth was above average in 2012–2014 & 2020–2021, while 2015–2019 & 2022 saw below-average growth.", fontsize=10, color="gray")
plt.tight_layout()


plt.show()

# Insight
print(f"""
The histogram shows that in 2012, 2013, 2014, 2020, and 2021, salary growth was above average,
whereas from 2015 to 2019 and in 2022, salary growth was below average.
This trend could be influenced by factors such as economic conditions, company policies, or industry demand during those years.
Additionally, external factors like inflation rates or global events may have also played a role in shaping salary trends.
Further analysis of specific job roles and tenure could provide deeper insights into these fluctuations.
""")

