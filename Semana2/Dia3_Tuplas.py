"""
# Crear tuplas
coordenadas = (4.6097, -74.0817)  # Bogotá
empleado = ("Cristian", "Bucaramanga", 4200000)

# Desempaquetado — muy usado en Python
lat, lon = coordenadas
nombre, ciudad, salario = empleado

print(f"{nombre} vive en {ciudad}")  # Cristian vive en Bucaramanga

# Tuplas como registros en una lista
ventas = [
    ("Enero", 15000000, 320),
    ("Febrero", 18500000, 410),
    ("Marzo", 12000000, 280),
]
for mes, ingresos, unidades in ventas:
    print(f"{mes}: ${ingresos:,.0f} — {unidades} unidades")

# Inmutabilidad — esto da error:
# coordenadas[0] = 5.0  → TypeError
"""
#EJERCICIO
"""
Crea una lista de tuplas con datos de al menos 5 departamentos de Colombia: (nombre, capital, 
poblacion, area_km2). Luego itera sobre ellos e imprime una ficha formateada de cada uno. Usa 
desempaquetado en el loop. Calcula cuál tiene mayor densidad poblacional (población / área).
"""
departamentos = [
    ("Antioquia", "Medellín", 6700000, 63612),
    ("Cundinamarca", "Bogotá", 8000000, 24210),
    ("Santander", "Bucaramanga", 2200000, 30537),
    ("Valle del Cauca", "Cali", 4500000, 22140),
    ("Atlántico", "Barranquilla", 2500000, 3388),
]
#1
def info_print(departamento, ciudad, poblacion, area_km2):

    densidad = round(poblacion / area_km2,1)

    print(f"---{departamento}---")
    print(f"Capital: {ciudad}")
    print(f"Poblacion: {poblacion:,}")
    print(f"Area: {area_km2:,}")
    print(f"Densidad: {densidad}\n")

for departamento,ciudad,poblacion,area_km2 in departamentos:
    info_print(departamento,ciudad,poblacion,area_km2)
#2
mayor = max(departamentos, key=lambda d: d[2] / d[3])
nombre, ciudad, poblacion, area_km2 = mayor
densidad = round(poblacion / area_km2,1)
print(f"Mayor densidad: {nombre} con {densidad} hab/km2")