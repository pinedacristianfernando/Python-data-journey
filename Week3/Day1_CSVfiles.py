"""
import csv

# Writing a CSV file
employees = [
    ["name", "city", "salary_cop", "department"],
    ["Ana Torres", "Bogotá", 4500000, "Engineering"],
    ["Carlos Ruiz", "Medellín", 3200000, "Marketing"],
    ["Laura Gómez", "Bucaramanga", 5100000, "Engineering"],
]

with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

# Reading a CSV file
with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # reads each row as a dict
    for row in reader:
        print(f"{row['name']} — {row['city']} — ${int(row['salary_cop']):,}")
"""
#Exercise
"""
Create a CSV file called colombian_cities.csv with at least 6 cities and columns: city, department, 
population, avg_salary_cop. Then read it back and print a formatted summary for each city. Use DictReader 
so you access columns by name.
"""
import csv
cities = [
    ["city", "department", "population", "avg_salary_cop"],
    ["Bogotá", "Cundinamarca", 8000000, 4500000],
    ["Medellín", "Antioquia", 2500000, 3800000],
    ["Cali", "Valle del Cauca", 2200000, 3100000],
    ["Barranquilla", "Atlántico", 1200000, 3400000],
    ["Bucaramanga", "Santander", 600000, 3200000],
    ["Cartagena", "Bolívar", 1000000, 2900000],
]
with open("week3_day1_colombian_cities.csv","w",newline="",encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(cities)
print("CSV created successfully")

# Read the CSV back
with open("week3_day1_colombian_cities.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['city']} ({row['department']}) — Pop: {int(row['population']):,} "
              f"— Avg salary: ${int(row['avg_salary_cop']):,}")