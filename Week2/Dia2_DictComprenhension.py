# De lista a diccionario
ciudades = ["Bogotá", "Medellín", "Cali", "Bucaramanga"]
poblaciones = [8000000, 2500000, 2200000, 600000]

# zip() une dos listas en pares
ciudad_poblacion = {c: p for c, p in zip(ciudades, poblaciones)}
# → {"Bogotá": 8000000, "Medellín": 2500000, ...}

# Transformar un diccionario existente
en_millones = {ciudad: round(pob / 1_000_000, 1)
               for ciudad, pob in ciudad_poblacion.items()}
# → {"Bogotá": 8.0, "Medellín": 2.5, ...}

# Con condición — solo ciudades grandes
grandes = {c: p for c, p in ciudad_poblacion.items() if p > 1_000_000}

# Estructura general:
# {clave: valor for elemento in iterable if condicion}

#EJERCICIO
"""
Tienes una lista de productos de una tienda: [("café", 8500), ("arepa", 1200), ("aguardiente", 35000),
 ("empanada", 2500), ("bandeja paisa", 25000)]. Usa dict comprehensions para: 1) crear un diccionario 
 producto-precio, 2) crear uno solo con productos que cuesten más de $5000, 3) crear uno con los precios
 convertidos a USD.
"""
productos = [("café", 8500), ("arepa", 1200), ("aguardiente", 35000), ("empanada", 2500),
           ("bandeja paisa", 25000)]
#1
prod_prec = {producto: precio for producto, precio in productos}
print(prod_prec)
#2
prec_filt = {producto: precio for producto, precio in productos if precio > 5000}
print(prec_filt)
#3
prec_usd = {producto : round(precio/4200,1) for producto, precio in productos}
print(prec_usd)