# Day 25
# Pandas Library


import pandas as pd
import numpy as np

# ---------------------------------------------------
# 1. Create DataFrame
# ---------------------------------------------------

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Vijay", "Neha", "Rohan", "Kiran"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "Salary": [55000, 45000, 65000, 60000, np.nan, 48000, 70000, 58000],
    "Age": [25, 28, 24, 30, 27, 26, 32, 29],
    "Joining_Date": [ "2021-01-15", "2020-05-20", "2022-03-10", "2019-07-12", 
                     "2021-09-01", "2023-01-18", "2018-11-25", "2022-06-30" ],
    "Performance": ["Good", "Average", "Excellent", "Good",
                    "Average", "Good", "Excellent", "Good"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# ---------------------------------------------------
# 2. Basic Information
# ---------------------------------------------------

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInformation:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ---------------------------------------------------
# 3. Check Missing Values
# ---------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# ---------------------------------------------------
# 4. Fill Missing Salary
# ---------------------------------------------------

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter Filling Missing Salary:")
print(df)


# ---------------------------------------------------
# 5. Convert Joining_Date into Datetime
# ---------------------------------------------------

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\nDate Data Type:")
print(df["Joining_Date"].dtype)


# ---------------------------------------------------
# 6. Create New Column using apply()
# ---------------------------------------------------

df["Salary_After_Bonus"] = df["Salary"].apply(
    lambda x: x * 1.10
)

print("\nSalary After Bonus:")
print(df[["Name", "Salary", "Salary_After_Bonus"]])


# ---------------------------------------------------
# 7. Create Salary Category using np.where()
# ---------------------------------------------------

df["Salary_Category"] = np.where(
    df["Salary"] >= 60000,
    "High",
    "Low"
)

print("\nSalary Category:")
print(df[["Name", "Salary", "Salary_Category"]])


# ---------------------------------------------------
# 8. Filtering
# ---------------------------------------------------

high_salary = df[df["Salary"] > 60000]

print("\nEmployees with Salary > 60000:")
print(high_salary)


# Multiple Conditions
it_employees = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 55000)
]

print("\nIT Employees with Salary > 55000:")
print(it_employees)


# ---------------------------------------------------
# 9. loc
# ---------------------------------------------------

print("\nUsing loc:")
print(df.loc[df["Salary"] > 60000, ["Name", "Department", "Salary"]])


# ---------------------------------------------------
# 10. iloc
# ---------------------------------------------------

print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])


# ---------------------------------------------------
# 11. Sorting
# ---------------------------------------------------

sorted_df = df.sort_values(
    by="Salary",
    ascending=False
)

print("\nEmployees Sorted by Salary:")
print(sorted_df[["Name", "Salary"]])


# ---------------------------------------------------
# 12. GroupBy
# ---------------------------------------------------

dept_avg_salary = df.groupby(
    "Department"
)["Salary"].mean()

print("\nAverage Salary by Department:")
print(dept_avg_salary)


# ---------------------------------------------------
# 13. GroupBy + Multiple Aggregations
# ---------------------------------------------------

dept_summary = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Employee_Count=("Employee_ID", "count")
)

print("\nDepartment Summary:")
print(dept_summary)


# ---------------------------------------------------
# 14. Value Counts
# ---------------------------------------------------

print("\nEmployees by Department:")
print(df["Department"].value_counts())

print("\nPerformance Distribution:")
print(df["Performance"].value_counts())


# ---------------------------------------------------
# 15. Unique and nunique
# ---------------------------------------------------

print("\nUnique Departments:")
print(df["Department"].unique())

print("\nNumber of Departments:")
print(df["Department"].nunique())


# ---------------------------------------------------
# 16. String Operations
# ---------------------------------------------------

df["Name"] = df["Name"].str.upper()

print("\nNames in Uppercase:")
print(df["Name"])


# ---------------------------------------------------
# 17. Extract Year from Date
# ---------------------------------------------------

df["Joining_Year"] = df["Joining_Date"].dt.year

print("\nJoining Year:")
print(df[["Name", "Joining_Date", "Joining_Year"]])


# ---------------------------------------------------
# 18. Pivot Table
# ---------------------------------------------------

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Performance",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot)


# ---------------------------------------------------
# 19. Remove Duplicate Rows
# ---------------------------------------------------

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)


# ---------------------------------------------------
# 20. Rename Columns
# ---------------------------------------------------

df = df.rename(
    columns={"Salary": "Monthly_Salary"}
)

print("\nRenamed Column:")
print(df.columns)


# ---------------------------------------------------
# 21. Merge Example
# ---------------------------------------------------

location_data = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Location": [
        "Pune", "Mumbai", "Pune", "Delhi",
        "Pune", "Mumbai", "Delhi", "Pune"
    ]
})

df = pd.merge(
    df,
    location_data,
    on="Employee_ID",
    how="left"
)

print("\nAfter Merge:")
print(df)


# ---------------------------------------------------
# 22. Final Result
# ---------------------------------------------------

print("\nFinal Employee Data:")
print(df)


# ---------------------------------------------------
# 23. Save to CSV
# ---------------------------------------------------

df.to_csv("employee_analysis.csv", index=False)

print("\nFile saved successfully!")
