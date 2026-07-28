"""
df["salary_zscore"] = (df["salary_usd"] - np.mean(df["salary_usd"])) / np.std(df["salary_usd"])

df["salary_tier"] = np.where(df["salary_usd"] > 1000, "high", "standard")

df["pop_tier"] = np.select(
    [df["population"] < 500_000, df["population"] < 2_000_000],
    ["small", "medium"],
    default="large"
)
"""
from email.policy import default

#EXERCISE
"""
#1 Add a density_zscore column to your Week 5 cities DataFrame using NumPy mean/std.
#2 Add a density_tier column with np.where: "dense" above a threshold you choose, "sparse" otherwise.
#3 Use np.select to build a 3-tier pop_tier column (small / medium / large).
#4 Print only the rows where abs(density_zscore) > 2 — your density outliers.
#5 Open: design one more derived column a hiring team would find useful — something like a "cost-of-living 
adjusted salary" per city. Decide the formula yourself and justify it in a comment.
"""
import numpy as np
import pandas as pd

df = pd.read_csv("week5_project_colombian_cities.csv")

#1
df["density"] = df["population"] / df["area_km2"]
df["density_zscore"] = (df["density"] - np.mean(df["density"])) / np.std(df["density"])

#2
df["density_tier"] = np.where(df["density"] > 1000, "dense", "sparse")

#3
df["pop_tier"] = np.select(
    [df["population"] < 500_000, df["population"] < 2_000_000],
    ["small", "medium"],
    default="large"
)

#4
print(df[df["density_zscore"].abs() > 2])

#5
df["persons_per_hospital"] = np.round(df["population"] / df["hospitals"],2)
df["persons_per_hospital_tier"] = np.select(
    [df["persons_per_hospital"] < 25_000, df["persons_per_hospital"] < 35_000 ],
    ["low risk", "medium risk"],
    default = "high risk"
)
print(df["persons_per_hospital_tier"])
"""
A hiring team would use this to understand healthcare infrastructure pressure.
Cities with high persons_per_hospital ratio signal understaffed systems,
which affects quality of life and indirectly talent attraction.
"""
