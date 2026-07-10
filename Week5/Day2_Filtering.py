import pandas as pd

data = {
    "city": ["Bogotá", "Medellín", "Cali", "Bucaramanga", "Cartagena"],
    "department": ["Cundinamarca", "Antioquia", "Valle del Cauca", "Santander", "Bolívar"],
    "population": [8000000, 2500000, 2200000, 600000, 1000000],
    "avg_salary_cop": [4500000, 3800000, 3100000, 3200000, 2900000],
}
df = pd.DataFrame(data)

# Boolean mask — creates a Series of True/False
mask = df["population"] > 1000000
print(mask)         # True, True, True, False, False...
print(df[mask])     # only rows where mask is True

# Shorthand — inline condition
big_cities = df[df["population"] > 1000000]

# Multiple conditions — MUST use parentheses
high_salary = df[
    (df["avg_salary_cop"] > 3000000) &
    (df["population"] > 500000)
]

# Select specific columns
df[["city", "population"]]           # two columns → DataFrame
df["city"]                           # one column → Series

# Combine filter + column selection
df[df["population"] > 1000000][["city", "population"]]

# .query() — SQL-like syntax, very readable
df.query("population > 1000000 and avg_salary_cop > 3000000")

#EXERCISE
"""
Using your DataFrame from Day 1: 1) filter cities with population over 1M, 2) filter cities where 
salary is above the average salary, 3) combine both conditions, 4) select only city and avg_salary_cop 
for cities in "Antioquia" or "Cundinamarca", 5) use .query() to replicate one of the filters.
"""
#1
big_population = df[df["population"] > 1000000]
print("1) The cities with 1000000 population or more are:\n",big_population, "\n")

#2
average_salary = df["avg_salary_cop"].mean()
big_salary = df[df["avg_salary_cop"] > average_salary]
print("2) The above salary cities are:\n",big_salary, "\n")

#3
big_population_salary = df[
    (df["population"] > 1000000) &
    (df["avg_salary_cop"] > average_salary)
]
print("3) The cities with population bigger than 1000000 and above average salary are:\n",
      big_population_salary, "\n")

#4
condition = df.query("department in ['Cundinamarca', 'Antioquia']")[["city","avg_salary_cop"]]
print("4) city and avg_salary_cop for cities in 'Antioquia' or 'Cundinamarca':\n", condition, "\n")

#5
replicate = df.query(f"population > 1000000 and avg_salary_cop > {average_salary}")
print("5) The same question 3, but query:\n", replicate)