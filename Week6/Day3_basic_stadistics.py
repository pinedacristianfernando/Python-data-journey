import numpy as np

salaries_cop = np.array([1_800_000, 2_500_000, 3_200_000,
                         4_800_000, 25_000_000])

# 1. Mean, median, std in one pass
mean_s, median_s, std_s = salaries_cop.mean(), np.median(salaries_cop), salaries_cop.std()

# 2. Percentiles — any cut point you want
percentile50 = np.percentile(salaries_cop, 50)

# 3. Z-score for every element — how many std devs from the mean
z_scores = (salaries_cop - mean_s) / std_s

# 4. Boolean mask built directly from the z-score
outliers = salaries_cop[np.abs(z_scores) > 2]

#EXERCISE
"""
#1 Using your Week 5 dataset of 20 Colombian cities, compute mean, median, and std dev of the salary column.
#2 Compute the 25th, 50th, 75th, and 90th percentile of the population column.
#3 Flag any city whose salary is more than 2 standard deviations from the mean.
#4 Compare mean vs median of the salary column — write a one-line comment explaining why they diverge, 
based on step 3.
#5 Open: you're reporting "average salary" to a stakeholder for a policy decision. Given the outliers 
you found, would you report the mean or the median — and why?
"""
import pandas as pd

df = pd.read_csv("week5_project_colombian_cities.csv")

#1
salary = df["avg_salary_cop"].to_numpy()
mean = np.mean(salary).round(2)
print(f"The mean of the salary column is {mean}")
median = np.median(salary).round(2)
print(f"The median of the salary column is {median}")
std = np.std(salary).round(2)
print(f"The standard deviation of the salary column is {std}\n")

#2
population = df["population"].to_numpy()
p25, p50 ,p75, p90 = np.percentile(population, [25, 50, 75, 90]).round(2)
print(f"The percentile 25 is: {p25}, 50 is: {p50}, 75 is: {p75}, 90 is: {p90}\n")

#3
z_scores_salary = (salary - mean) / std
city = df["city"].to_numpy()
outliers_salary = (z_scores_salary > 2) | (z_scores_salary < -2)
print(f"The cities whose salary is more than 2 standard deviations from the mean is {city[outliers_salary]}")

#4
"""
The mean and median diverge because Bogotá's salary (4,500,000) pulls the mean upward. Most cities earn 
between 2,400,000 and 3,000,000, so the median better represents the typical city.
"""

#5
"""
I would report the median because Bogotá is an outlier that inflates the mean, making it unrepresentative 
of what a typical Colombian city earns.
"""



