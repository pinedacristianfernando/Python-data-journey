import pandas as pd

"""
# Check for nulls
df.isnull().sum()          # nulls per column
df.isnull().any()          # which columns have any null

# Handle nulls
df.dropna()                        # drop rows with any null
df.dropna(subset=["population"])   # drop only if population is null
df["salary"].fillna(0)             # fill nulls with 0
df["salary"].fillna(df["salary"].mean())  # fill with mean

# Duplicates
df.duplicated().sum()              # count duplicates
df.drop_duplicates()               # remove duplicate rows
df.drop_duplicates(subset=["city"])  # duplicates by city column

# Fix data types
df["population"] = df["population"].astype(int)
df["salary_str"] = df["salary_str"].str.replace(",", "").astype(float)

# String cleaning
df["city"] = df["city"].str.strip()        # remove whitespace
df["city"] = df["city"].str.lower()        # lowercase
df["city"] = df["city"].str.title()        # Title Case
df["dept"] = df["dept"].str.replace("  ", " ")  # fix double spaces

# Add calculated columns
df["salary_usd"] = df["avg_salary_cop"] / 4200
df["density"] = df["population"] / df["area_km2"]
"""

#EXERCISE
""""
 Create a messy version of your cities DataFrame with: some null values in salary, a duplicate row, 
 inconsistent city names ("bogotá", "BOGOTÁ", " Bogotá "), and salary stored as strings with commas 
 ("3,200,000"). Then clean it: fix nulls, remove duplicates, standardize city names, convert salary 
 to float, and add salary_usd and density columns.
"""
messy_data = {
    "city": ["bogotá", "BOGOTÁ", " Bogotá ", "Medellín", "Cali", "Barranquilla", "Bucaramanga", "Cartagena"],
    "department": ["Cundinamarca", "Cundinamarca", "Cundinamarca", "Antioquia", "Valle del Cauca", "Atlántico", "Santander", "Bolívar"],
    "population": [8000000, 8000000, 8000000, 2500000, 2200000, 1200000, 600000, 1000000],
    "avg_salary_cop": ["4,500,000", "4,500,000", "4,500,000", "3,800,000", None, "3,400,000", "3,200,000", "2,900,000"],
    "area_km2": [1587, 1587, 1587, 380, 564, 154, 165, 609],
}
df = pd.DataFrame(messy_data)
print(df,"\n")

#Removing nulls
print(df.isnull().sum(),"\n") #Confirm where are the nulls
df = df.dropna(subset = ["avg_salary_cop"]) #Dropped the null rows

#Standard data
df["city"] = df["city"].str.strip().str.lower().str.title().str.replace("  ", " ")
df["department"] = df["department"].str.strip().str.lower().str.title().str.replace("  ", " ")

df["avg_salary_cop"] = df["avg_salary_cop"].str.replace(",", "").astype(float)

#Removing duplicates
print("The number of duplicates is: ",df.duplicated().sum(),"\n")
df = df.drop_duplicates(subset=["city"], keep="first")

#Add salary_usd and density column
df["salary_usd"] = df["avg_salary_cop"] / 4000
df["density"] = df["population"] / df["area_km2"]

print(df)


