# Unit 3 (Power BI) - Work Report

**Submitted By:**

2021UCA1536 - Aparna Srivastava

2021UCA1804 - Pulkit Batra

2021UCA1814 - Muskan Sinha

In Unit 3, we focused on Power BI, a powerful business analytics tool that provides interactive visualizations with self-service business intelligence capabilities. Our work involved learning how to connect to data, perform data transformations, and visually explore data to find insights.

# Dataset

Dataset used: [https://drive.google.com/drive/folders/18mQalCEyZypeV8TJeP3SME_R6qsCS2Og](https://drive.google.com/drive/folders/18mQalCEyZypeV8TJeP3SME_R6qsCS2Og)

1. **EmpID**: Unique identifier for each employee.
2. **Age**: Age of the employee.
3. **AgeGroup**: Categorization of age into groups (e.g., young, middle-aged, senior).
4. **Attrition**: Indicates whether the employee has left the company (Yes/No).
5. **BusinessTravel**: Frequency of business travel for the employee (e.g., Travel_Rarely, Travel_Frequently, Non-Travel).
6. **DailyRate**: Daily rate of pay for the employee.
7. **Department**: Department in which the employee works.
8. **DistanceFromHome**: Distance of employee's residence from the workplace.
9. **Education**: Level of education attained by the employee.
10. **EducationField**: Field of education of the employee.
11. **EmployeeCount**: Number of employees (usually 1 for all records).
12. **EmployeeNumber**: Unique identifier assigned to each employee.
13. **EnvironmentSatisfaction**: Satisfaction level of the employee with their working environment.
14. **Gender**: Gender of the employee.
15. **HourlyRate**: Hourly rate of pay for the employee.
16. **JobInvolvement**: Level of involvement of the employee in their job role.
17. **JobLevel**: Level of the employee's job within the organizational hierarchy.
18. **JobRole**: Role or position of the employee within the company.
19. **JobSatisfaction**: Satisfaction level of the employee with their job.
20. **MaritalStatus**: Marital status of the employee.
21. **MonthlyIncome**: Monthly income of the employee.
22. **SalarySlab**: Categorization of monthly income into salary slabs.
23. **MonthlyRate**: Monthly rate of pay for the employee.
24. **NumCompaniesWorked**: Number of companies the employee has worked for previously.
25. **Over18**: Indicates whether the employee is over 18 years old (Yes/No).
26. **OverTime**: Indicates whether the employee works overtime (Yes/No).
27. **PercentSalaryHike**: Percentage increase in salary for the employee.
28. **PerformanceRating**: Performance rating of the employee.
29. **RelationshipSatisfaction**: Satisfaction level of the employee with their relationships at work.
30. **StandardHours**: Standard number of working hours (usually 80 for all records).
31. **StockOptionLevel**: Level of stock options granted to the employee.
32. **TotalWorkingYears**: Total number of years the employee has been working.
33. **TrainingTimesLastYear**: Number of times the employee was trained last year.
34. **WorkLifeBalance**: Level of balance between work and personal life for the employee.
35. **YearsAtCompany**: Number of years the employee has been with the current company.
36. **YearsInCurrentRole**: Number of years the employee has been in their current role.
37. **YearsSinceLastPromotion**: Number of years since the employee's last promotion.
38. **YearsWithCurrManager**: Number of years the employee has been with their current manager.

# Data Cleaning

## Handling Null Values in "YearsWithCurrManager" Column

- Identified and addressed null values in the "YearsWithCurrManager" column.
- Filtered out rows where "YearsWithCurrManager" was null to ensure data completeness.
- Data validation was performed to verify the effectiveness of the cleaning process.
- The dataset was refreshed to update with the cleaned version.

## Mapping "Attrition" Column to 0 and 1

- Replaced textual values in the "Attrition" column with numerical equivalents.
    - Replaced "Yes" with 1.
    - Replaced "No" with 0.
- Data validation was performed to ensure all instances of "Attrition" were correctly represented as 0s and 1s.
- The dataset was refreshed to apply the changes made to the "Attrition" column.

# Data Visualisation

We then moved to data visualization. We learned how to use Power BI's drag-and-drop capabilities to create a variety of charts, including bar charts, line charts, and scatter plots. We explored how to customize these visualizations, add filters, and create dashboards.

![PowerBIAssignmentPulkit_page-0001.jpg](Unit%203%20(Power%20BI)%20-%20Work%20Report%2044698294acba4cc38bd141f0a9f87ea8/PowerBIAssignmentPulkit_page-0001.jpg)

## **HR Analytics Dashboard - Attrition Insights**

**KPIs:**

- **Attrition Rate:** 16.17%
- **Applicants by Education:**
    - Bar Chart: Visualizing distribution across different education levels.
- **Applicants by Age:**
    - Bar Chart: Visualizing distribution across different age groups.
- **Average Age:** 37 years
- **Average Salary:** 7K
- **Average Years:** 7 years
- **Attrition by:**
    - Education: Bar Chart showing number of leavers categorized by education.
    - Age: Bar Chart showing number of leavers categorized by age group.
    - Job Role: Bar Chart showing number of leavers categorized by job role.
    - Salary Slab: Bar Chart showing number of leavers categorized by salary bracket.
    - Years at Company: Bar Chart showing number of leavers categorized by years spent in the company.

**Key Observations:**

- **Gender Discrepancy:** Attrition rate higher for females (14.85%) than males (11.35%).
- **Age Vulnerability:** Highest attrition rate in 25-35 age group (46.51%).
- **Job Role Impact:** Laboratory Technician role faces highest attrition (21.67%).
- **Salary and Retention:** Upto 5k salary slab witnesses highest turnover (70%).
- **New Hires at Risk:** Employees with less than 2 years of tenure show higher attrition (53.85%).

**Data Visualization:**

- Bar charts: Applicant & leaver distribution by education, age, job role, salary slab, years at company.
- Line charts: Average age, average salary, average years of employees.
- Pie charts: Employee distribution by gender.
- Tables: Raw data for all KPIs, detailed attrition breakdown by job role and years at company.

Finally, we learned how to publish our reports to the Power BI service, where we could share them with others and schedule data refreshes. Throughout this unit, we applied these skills to real-world data, gaining practical experience in business intelligence and data visualization.

Link to final Dashboard: [https://app.powerbi.com/groups/me/reports/a724d2a2-8fb2-46e9-8d4b-22de9df4afc3/ReportSection?experience=power-bi](https://app.powerbi.com/groups/me/reports/a724d2a2-8fb2-46e9-8d4b-22de9df4afc3/ReportSection?experience=power-bi)