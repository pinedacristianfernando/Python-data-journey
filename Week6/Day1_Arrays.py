import numpy as np

cities = ["Bogota", "Medellin", "Cali", "Bucaramanga", "Cartagena"]
population = np.array([8_000_000, 2_500_000, 2_200_000, 600_000, 1_000_000])
avg_salary_cop = np.array([4_500_000, 3_800_000, 3_100_000, 3_200_000, 2_900_000])

# 1. Arithmetic with a scalar broadcasts to every element
salary_usd = avg_salary_cop / 4100

# 2. Compound growth over multiple years using exponentiation
population_in_5y = population * (1.018 ** 5)

# 3. np.where — vectorized if/else across the whole array
salary_tier = np.where(avg_salary_cop > 3_500_000, "high", "standard")

# 4. np.argsort — get the indices that would sort the array
order = np.argsort(population)[::-1]      # descending
print([cities[i] for i in order])

# 5. Elementwise multiplication between two arrays of the same shape
salary_mass = population * avg_salary_cop

#EXERCISE
"""
#1 Project each city's population in 5 years at 1.8% annual growth.
#2 Convert avg_salary_cop to USD (rate 4,100) and count how many cities exceed USD 800/month.
#3 Build a salary_tier array: "high" if salary_cop > 3,500,000, else "standard".
#4 Estimate population density (population / area_km2, invent realistic areas) and rank cities densest 
to sparsest.
Open: combine population and salary to estimate each city's "total salary mass." Which city leads — even 
if it isn't the one with the highest individual salary?
"""
#1
population_in_5years = np.round(population * (1.018 ** 5),2)
print(f"The population for each city en the next 5 years is: \n {population_in_5years}\n")
#2
salary_usd = avg_salary_cop / 4100
count = np.sum(salary_usd > 800)
print(f"Cities exceeding USD 800/month: {count}\n")
#3
salary_tier = np.where(avg_salary_cop > 3_500_000, "high", "standard")
print(f"Salary tier is: \n {salary_tier}\n")
#4
areas_km2 = np.array([1587, 380, 564, 165, 609])
density = population / areas_km2
order_density = np.argsort(density)[::-1]
print("The densest to sparsest rank is:")
for i in order_density:
    print(f"{cities[i]}: {density[i]:,.0f} people/km2")
print("")
#5
salary_mass = avg_salary_cop * population
order_salary = np.argsort(salary_mass)[::-1]
print("The salary/population rank is:")
for i in order_salary:
    print(f"{cities[i]}: {salary_mass[i]:,.0f} COP")



