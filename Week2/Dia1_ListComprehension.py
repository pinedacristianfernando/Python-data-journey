# Forma clásica con loop
salarios_cop = [2800000, 4500000, 1900000, 6200000, 3100000]
salarios_usd = []
for s in salarios_cop:
    salarios_usd.append(round(s / 4200, 2))

# Forma pythonica con list comprehension — mismo resultado
salarios_usd = [round(s / 4200, 2) for s in salarios_cop]

# Con condición — solo los que superan $500 USD
salarios_altos = [round(s / 4200, 2) for s in salarios_cop if s / 4200 > 500]

# Estructura general:
# [expresion for elemento in iterable if condicion]

#EJEERCICIO
"""
Tienes esta lista de ciudades colombianas y sus poblaciones: [("Bogotá", 8000000), ("Medellín", 2500000), 
("Cali", 2200000), ("Barranquilla", 1200000), ("Bucaramanga", 600000)]. Usa list comprehensions para: 1) 
extraer solo los nombres, 2) extraer solo las ciudades con más de 1 millón de habitantes, 3) crear una 
lista de strings con formato "Bogotá: 8,000,000 hab".
"""
cuidades_poblacion =[("Bogotá", 8000000), ("Medellín", 2500000), ("Cali", 2200000),
           ("Barranquilla", 1200000), ("Bucaramanga", 600000)]
#1
cuidades =  [nombre for nombre,poblacion in cuidades_poblacion]
print(cuidades)
#2
cuidades_mill = [nombre for nombre,poblacion in cuidades_poblacion if poblacion>1000000]
print(cuidades_mill)
#3
info_cuidad = [f"{nombre}: {poblacion:,} hab." for nombre,poblacion in cuidades_poblacion]
for linea in info_cuidad:
    print(linea)
