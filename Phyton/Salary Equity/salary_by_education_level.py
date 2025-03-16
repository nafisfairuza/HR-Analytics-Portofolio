import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"Employee.csv")

education_mapping = {
    1: "High School",
    2: "Associate's Degree",
    3: "Bachelor's Degree",
    4: "Master's Degree",
    5: "PhD"
}
df['Education'] = df['Education'].map(education_mapping)

# 1. Violin Plot: Distribution of Salary by Education Level
plt.figure(figsize=(10, 6))
sns.violinplot(x='Education', y='Salary', data=df, palette='Set2', inner='quartile')
plt.title('Salary Distribution by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Salary')
plt.xlabel("Education Level\n\nInsight: The violin plot shows that the highest salaries are found at the High School education level, contrary to common expectations.", fontsize=10, color="gray")
plt.xticks(rotation=15)
plt.show()

# 2. Job Role with Highest Salary in Each Education Level
print("\n--max salary by education level--")
top_salary_per_education = df.loc[df.groupby('Education', dropna=True)['Salary'].idxmax()]
top_salary_per_education = top_salary_per_education[['Education', 'JobRole', 'YearsAtCompany', 'Salary']]
top_salary_per_education = top_salary_per_education.sort_values(by="Salary", ascending=False)
print(top_salary_per_education)

#3. Job Role with Lowest Salary in Each Education Level
print("\n--min salary by education level--")
low_salary_per_education = df.loc[df.groupby('Education', dropna=True)['Salary'].idxmin()]
low_salary_per_education = low_salary_per_education[['Education', 'JobRole', 'YearsAtCompany', 'Salary']]
low_salary_per_education = low_salary_per_education.sort_values(by="Salary", ascending=True)
print(low_salary_per_education)

print(f"""
Insight:
The violin plot shows the salary distribution by education level, with some outliers.
From the graph, it is clear that the highest salary does not belong to PhD holders but to those with a High School education.
This is confirmed in the table, where the highest-paying positions are dominated by Analytics Managers, one of whom has a High School education.
Meanwhile, the lowest-paying positions are mostly occupied by Data Scientists and Recruiters, especially at lower education levels.
Interestingly, although higher education is generally assumed to correlate with higher salaries,
the data shows that PhD holders actually have lower top salaries compared to other education levels.
One possible reason is that many PhD graduates work in academic or research fields, which may offer lower compensation than roles in business or technology industries.
""")
