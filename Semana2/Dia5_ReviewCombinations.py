# Diccionario de listas — estructura muy común en data
from pip._internal.commands import index

ventas_por_ciudad = {
    "Bogotá":      [15000000, 18000000, 12000000],
    "Medellín":    [9000000,  11000000, 10500000],
    "Bucaramanga": [4200000,  5100000,  3800000],
}

# Crea un diccionario promedios con el promedio de ventas de cada ciudad
promedios = {
    ciudad: round(sum(ventas) / len(ventas), 0)
    for ciudad, ventas in ventas_por_ciudad.items()
}
print(promedios)

# Set comprehension — ciudades con promedio > 10 millones
ciudades_lista = [c for c, p in promedios.items() if p > 10_000_000]
print(ciudades_lista)

# Crear un set con ciudades_top
ciudades_top =  set(ciudades_lista)
print(ciudades_top)

#  Usa max() para encontrar la ciudad con mayor promedio, desempaqueta el resultado e imprímelo
mayor = max(promedios, key=promedios.get)
mayor_ventas = promedios[mayor]
print(f"{mayor} tiene mayor promedio de ventas: {mayor_ventas:,.0f}")
