# Eliminar duplicados automáticamente
ciudades_visitas = ["Bogotá", "Medellín", "Bogotá", "Cali", "Medellín", "Cartagena"]
unicas = set(ciudades_visitas)
# → {"Bogotá", "Medellín", "Cali", "Cartagena"}

# Operaciones de conjuntos — muy útil para análisis
clientes_enero = {"Ana", "Carlos", "Luis", "María"}
clientes_febrero = {"Carlos", "María", "Pedro", "Juan"}

# Clientes en ambos meses
ambos = clientes_enero & clientes_febrero      # {"Carlos", "María"}

# Clientes de enero que no volvieron
no_volvieron = clientes_enero - clientes_febrero  # {"Ana", "Luis"}

# Todos los clientes únicos
todos = clientes_enero | clientes_febrero      # todos juntos

print(f"Clientes recurrentes: {ambos}")
print(f"Clientes perdidos: {no_volvieron}")

#EJERCICIO
"""
Tienes dos listas de municipios que participaron en dos programas distintos del gobierno colombiano. 
Usa sets para encontrar: 1) municipios en ambos programas, 2) municipios solo en el primero, 3) 
municipios solo en el segundo, 4) total de municipios únicos. Inventa los datos con al menos 8 municipios 
por lista.
"""
programa1 = set(["San Gil", "Curiti", "Socorro", "Barichara", "Valle", "Bucaramanga", "Cartagena"])
programa2 = set(["Chia", "Bogota", "Barichara", "San Gil", "Los Santos", "Madrid", "Valle"])
#1
ambos = programa1 & programa2
print(f"Municipios en ambos programas: {ambos}")
#2
solo_primero = programa1 - programa2
print(f"Municipios que solo participaron en el programa1 y no en el programa2: {solo_primero}")
#3
solo_segundo = programa2 - programa1
print(f"Municipios que solo participaron en el programa2 y no en el programa1: {solo_segundo}")
#4
unicos = programa1 | programa2
print(f"Los municipios que participan en ambos programas: {unicos}")