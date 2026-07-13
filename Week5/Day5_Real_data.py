import pandas as pd
"""
# Read a CSV file
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", encoding="utf-8")
df = pd.read_csv("data.csv", sep=";")          # semicolon separator
df = pd.read_csv("data.csv", decimal=",")      # European decimal comma

# First thing always — explore
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Save cleaned data
df.to_csv("clean_data.csv", index=False, encoding="utf-8")
df.to_json("clean_data.json", orient="records", indent=2)
"""
#EXERCISE
"""
Go to datos.gov.co and download any CSV dataset that interests you (population, economy, health, 
education — anything Colombian). Load it with pd.read_csv(), run the full exploration, identify and 
fix at least 2 data quality issues, and answer 3 questions about the data using filter and groupby.
"""
df = pd.read_csv("Beneficiarios_del_Ministerio_de_las_Culturas_y_los_Saberes_20260712.csv", encoding="utf-8-sig")
print(df.shape,"\n")
print(df.head(),"\n")
print(df.info(),"\n")
print(df.describe(),"\n")
print(df.isnull().sum(),"\n")

df["vigencia"] = df["vigencia"].str.replace(",","").astype(int)
df["femenino"] = df["femenino"].str.replace(",","").astype(int)
df["masculino"] = df["masculino"].str.replace(",","").astype(int)
df["infancia 6 a 11 años"] = df["infancia 6 a 11 años"].str.replace(",","").astype(int)
df["adolescencia 12 a 17 años"] = df["adolescencia 12 a 17 años"].str.replace(",","").astype(int)
df["indígenas"] = df["indígenas"].str.replace(",","").astype(int)
df["total personas de atendidas"] = df["total personas de atendidas"].str.replace(",","").astype(int)

df = df[df["total personas de atendidas"] != 0]
print(df.shape,"\n")

coords = df["Centroide del municipio"].str.extract(r"POINT \(([^ ]+) ([^ ]+)\)")
df["longitud"] = coords[0].astype(float)
df["latitud"]  = coords[1].astype(float)

# Average "Total attended" (total personas de atendidas) per department (departamento)
total_attended = df.groupby("departamento")["total personas de atendidas"].sum().sort_values(ascending=False)
print("The attended people number per department is:\n", total_attended, "\n")

# Total number of indigenous people per department
ind = df.groupby("departamento")["indígenas"].sum().sort_values(ascending=False)
print("The indigenous people number per department is:\n", ind, "\n")

# Female percentage per department where validity is from 2025 to 2026
filtered = df[df["vigencia"] >= 2025]
fem = filtered.groupby("departamento").apply(
    lambda x: round(x["femenino"].sum()/x["total personas de atendidas"].sum() * 100,2)
).sort_values(ascending=False)
print("The female percentage per department is:\n", fem)

print(f"\n=== Dataset Summary ===")
print(f"Total records after cleaning: {len(df):,}")
print(f"Departments covered: {df['departamento'].nunique()}")
print(f"Years covered: {sorted(df['vigencia'].unique().tolist())}")
print(f"Total beneficiaries: {df['total personas de atendidas'].sum():,}")



