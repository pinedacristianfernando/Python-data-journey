import pandas as pd

# Create a DataFrame from a dict
data = {
    "city": ["Bogotá", "Medellín", "Cali", "Bucaramanga", "Cartagena"],
    "department": ["Cundinamarca", "Antioquia", "Valle del Cauca", "Santander", "Bolívar"],
    "population": [8000000, 2500000, 2200000, 600000, 1000000],
    "avg_salary_cop": [4500000, 3800000, 3100000, 3200000, 2900000],
}

df = pd.DataFrame(data)

# Basic exploration — always do this first
print(df.shape)       # (5, 4) → 5 rows, 4 columns
print(df.dtypes)      # column data types
print(df.head(3))     # first 3 rows
print(df.tail(2))     # last 2 rows
print(df.info())      # summary: types + nulls
print(df.describe())  # stats: mean, std, min, max

# Accessing a column → returns a Series
print(df["city"])
print(df["population"].mean())  # average population

# Accessing a row by index
print(df.iloc[0])   # first row by position
print(df.loc[0])    # first row by label (same here)

"""
First install Pandas: pip install pandas in your terminal. Then create a DataFrame with at least 8 
Colombian cities and columns: city, department, population, avg_salary_cop, area_km2. Run all the 
exploration methods (shape, dtypes, head, info, describe) and print the mean, max, and min of population.
"""
data_exercise = {
    "city": ["Barranquilla", "Pereira", "Manizales", "Santa Marta", "Ibagué", "Cúcuta", "Villavicencio", "Pasto"],
    "department": ["Atlántico", "Risaralda", "Caldas", "Magdalena", "Tolima", "Norte de Santander", "Meta", "Nariño"],
    "population": [1200000, 500000, 430000, 520000, 580000, 750000, 470000, 450000],
    "avg_salary_cop": [3400000, 2800000, 2900000, 2600000, 2700000, 2500000, 3000000, 2400000],
    "area_km2": [154, 702, 508, 2393, 1439, 1176, 1328, 1181],
}

exercise = pd.DataFrame(data_exercise)

print(exercise)
print(f"\nThe shape of the exercise data is {exercise.shape}\n")
print(f"The dtype of the exercise data is:\n{exercise.dtypes}\n")
print(f"The columns of the exercise data are {exercise.columns}\n")
print("The info of the exercise data is:")
print(exercise.info(), "\n")
print(f"The description of the exercise data is:\n{exercise.describe()}\n")

print(f"Population mean: {exercise['population'].mean():,.0f}")
print(f"Population min: {exercise['population'].min():,.0f}")
print(f"Population max: {exercise['population'].max():,.0f}")
