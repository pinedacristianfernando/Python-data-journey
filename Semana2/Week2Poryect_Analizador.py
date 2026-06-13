municipios = [
    ("Bogotá", "Cundinamarca", 8000000, 28000000),
    ("Medellín", "Antioquia", 2500000, 22000000),
    ("Cali", "Valle del Cauca", 2200000, 15000000),
    ("Barranquilla", "Atlántico", 1200000, 18000000),
    ("Bucaramanga", "Santander", 600000, 19000000),
    ("Cartagena", "Bolívar", 1000000, 14000000),
    ("Cúcuta", "Norte de Santander", 750000, 11000000),
    ("Pereira", "Risaralda", 480000, 16000000),
    ("Manizales", "Caldas", 420000, 17000000),
    ("Ibagué", "Tolima", 560000, 12000000),
]
# (municipio, departamento, poblacion, pib_per_capita)

#1 Dict comprehension → {municipio: poblacion} para todos
mun_pob = {municipio: poblacion for municipio,departamento, poblacion, pib_per_capita in municipios}

#2 List comprehension → municipios con PIB per cápita mayor al promedio
pib = [pib for municipio, departamento, poblacion, pib in municipios]
prom_pib = sum(pib)/len(pib)

#3 Set → departamentos únicos representados en la lista
dept = set([departamento for municipio, departamento, poblacion, pib in municipios])

#4 Tuplas + max() → top 3 municipios por población usando sorted()
top_pob = sorted(mun_pob.items(), key=lambda x: x[1], reverse=True)
top3 = top_pob[:3]

print("=== Analizador de Municipios en Colombia ===")
print(f"Total ciudades: {len(municipios)}")
print(f"Total departamentos unicos: {len(dept)}")
print(f"Municipios sobre el PIB promedio ({prom_pib:,.0f}):")
for municipio,departamento,poblacion,pib in municipios:
    if pib > prom_pib:
        print(f"- {municipio}")
print("Top 3 por población")
for i, (municipio,poblacion) in enumerate(top3, start=1):
    print(f"{i}. {municipio}:     {poblacion:,.0f} hab.")

