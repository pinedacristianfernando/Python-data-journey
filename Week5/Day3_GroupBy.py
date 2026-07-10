import pandas as pd

data = {
    "city": ["Bogotá", "Medellín", "Cali", "Bucaramanga", "Cartagena"],
    "department": ["Cundinamarca", "Antioquia", "Valle del Cauca", "Santander", "Bolívar"],
    "population": [8000000, 2500000, 2200000, 600000, 1000000],
    "avg_salary_cop": [4500000, 3800000, 3100000, 3200000, 2900000],
}
df = pd.DataFrame(data)

# Basic groupby — average salary per department
df.groupby("department")["avg_salary_cop"].mean()

# Multiple aggregations at once
df.groupby("department").agg(
    total_population=("population", "sum"),
    avg_salary=("avg_salary_cop", "mean"),
    city_count=("city", "count")
)

# Sort results
df.groupby("department")["population"].sum().sort_values(ascending=False)

# groupby + filter — departments with avg salary above 3.5M
dept_salary = df.groupby("department")["avg_salary_cop"].mean()
high_salary_depts = dept_salary[dept_salary > 3500000]

# reset_index() — converts groupby result back to a normal DataFrame
result = df.groupby("department")["population"].sum().reset_index()
print(result.columns)  # Index(['department', 'population'])

#EXCERSICE
"""
Using your DataFrame: 1) total population per department, 2) average salary per department sorted 
descending, 3) use .agg() to get count of cities, total population, and mean salary per department 
in one call, 4) find which department has the highest average salary, 5) add a region column (Norte, 
Centro, Sur) and group by it.
"""
#1
total_population = df.groupby("department")["population"].sum()
print("The total population per department is:\n", total_population, "\n")

#2
average_salary = df.groupby("department")["avg_salary_cop"].sum().sort_values(ascending=False)
print("The average salary per department is:\n", average_salary, "\n")

#3
agregation = df.groupby("department").agg(
    total_population=("population", "sum"),
    ave_salary=("avg_salary_cop", "mean"),
    city_count=("city", "count")
)
print("Get count of cities, total population, and mean salary per department in one call\n",
      agregation, "\n")

#4
max_salary = df.groupby("department")["avg_salary_cop"].max().idxmax()
print("The department with the maximum salary is:\n", max_salary, "\n")

#5
region_map = {
    "Cundinamarca": "Centro",
    "Antioquia": "Centro",
    "Valle del Cauca": "Sur",
    "Santander": "Norte",
    "Bolívar": "Norte"
}

df["region"] = df["department"].map(region_map)
print(df)