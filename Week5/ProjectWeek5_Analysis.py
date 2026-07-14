"""
Colombian cities analysis with Pandas.
"""
import pandas as pd

df = pd.read_csv("week5_project_colombian_cities.csv")

# 1. Full exploration: shape, info, describe, null check
# 2. Add columns: salary_usd, density (pop/area if available), category
# 3. Filter: major cities (pop > 1M), high salary (> avg)
# 4. Groupby region: total pop, avg salary, city count
# 5. Top 3 city by population, top 3 by salary
# 6. Save clean version to clean_cities.csv
# 7. Print a full summary report

#1
print(df.shape,"\n")
print(df.head(),"\n")
print(df.info(),"\n")
print(df.describe(),"\n")
print(df.isnull().sum(),"\n")

#2
df["salary_usd"] = df["avg_salary_cop"]/4000
df["density"] = df["population"]/df["area_km2"]
def category_city(population):
    if population >= 1000000:
        return "major"
    elif population >= 500000:
        return "medium"
    else:
        return "minor"
df["category"] = df["population"].apply(category_city)

#3
high_population_salary = df[
    (df["category"] == "major") &
    (df["avg_salary_cop"] > df["avg_salary_cop"].mean())
]
print(high_population_salary,"\n")

#4
total_population = df.groupby("region")["population"].sum()
print(total_population,"\n")
avg_salary = df.groupby("region")["avg_salary_cop"].mean().astype(int)
print(avg_salary,"\n")
city_count = df.groupby("region")["city"].count()
print(city_count,"\n")

#5
top3_population = df.nlargest(3, "population")[["city", "population"]]
print(top3_population,"\n")
top3_salary = df.nlargest(3, "avg_salary_cop")[["city", "avg_salary_cop"]]
print(top3_salary,"\n")

#6
df.to_csv("week5_project_clean_cities.csv", index=False, encoding="utf-8-sig")
print("Clean dataset saved.")

#7
print("=" * 50)
print("   COLOMBIAN CITIES ANALYSIS — SUMMARY REPORT")
print("=" * 50)

print(f"\n Dataset overview:")
print(f"   Total cities:        {len(df)}")
print(f"   Regions covered:     {df['region'].nunique()}")
print(f"   Departments covered: {df['department'].nunique()}")

print(f"\n Population:")
print(f"   Total:   {df['population'].sum():,.0f}")
print(f"   Average: {df['population'].mean():,.0f}")
print(f"   Largest: {df.loc[df['population'].idxmax(), 'city']} ({df['population'].max():,.0f})")
print(f"   Smallest:{df.loc[df['population'].idxmin(), 'city']} ({df['population'].min():,.0f})")

print(f"\n Salaries:")
print(f"   Avg COP: ${df['avg_salary_cop'].mean():,.0f}")
print(f"   Avg USD: ${df['salary_usd'].mean():,.2f}")
print(f"   Highest: {df.loc[df['avg_salary_cop'].idxmax(), 'city']}")
print(f"   Lowest:  {df.loc[df['avg_salary_cop'].idxmin(), 'city']}")

print(f"\n City categories:")
print(df["category"].value_counts().to_string())

print(f"\n Region with most people:")
top_region = df.groupby("region")["population"].sum().idxmax()
print(f"   {top_region}")

print(f"\n Clean dataset saved to: Week5/clean_cities.csv")
print("=" * 50)
