"""
salarios = [2800000, 4500000, 1900000, 6200000, 3100000]

# Lambda sola
retencion = lambda salario: salario * 0.04 if salario > 3000000 else 0

# map → aplica la lambda a todos los salarios
retenciones = list(map(retencion, salarios))
print(retenciones)  # [0, 180000, 0, 248000, 124000]

# filter → solo salarios que pagan retención
con_retencion = list(filter(lambda s: s > 3000000, salarios))
print(con_retencion)  # [4500000, 6200000, 3100000]

# Combinado — neto después de retención para quienes aplica
netos = list(map(lambda s: s - retencion(s), con_retencion))
print(netos)  # [4320000, 5952000, 2976000]
"""

#Ejercicio
"""
Tienes esta lista de salarios en COP: [1800000, 3500000, 2200000, 5000000, 4200000, 950000]. 
Usa map para convertirlos a USD (tasa 4200). Usa filter para quedarte solo con los mayores a $500 USD. 
Usa una lambda para calcular la retención (4% si > $750 USD). Imprime los resultados de cada paso.
"""

COP = [1800000, 3500000, 2200000, 5000000, 4200000, 950000]

cop_usd = lambda salario,tasa=4200: round(salario/tasa,2)
"""
    Convierte un monto de pesos colombianos a dólares.

    Args:
        salario (list): Valor en COP a convertir.
        tasa (int): Tasa de cambio COP/USD. Default: 4200.

    Returns:
        list: Equivalente en USD, redondeado a 2 decimales.

"""

convertido = list(map(cop_usd, COP))
"""
    Aplica la funcion cop_usd a la una lista
"""
print(convertido)

filtrado = list(filter(lambda s: s > 500, convertido))
"""
Muestra los valores mayores a 500 y elimina los que no cumplen la condicion
"""
print(filtrado)

funcion_retencion = lambda salario,tasa_ret=0.04: round(salario * tasa_ret,2) if salario > 750 else 0
"""
    Calcula la tasa de retencion si el salario es mayor a 750 USD.

    Args:
        salario (list): Valor en COP a calcular la retencion.
        tasa_ret (float): Valor retenido si el salario es mayor a 750 USD. Default: 0.04.

    Returns:
        list: Valores retenidos si se cumple la condicion.

"""
retenido = list(map(funcion_retencion, filtrado))
print(retenido)

import numpy as np
retenido  = np.array(retenido) #Vuelvo una matriz la lista de la retencion
filtrado = np.array(filtrado) #Vuelvo una matriz la lista de los salarios mayores a 500
neto = retenido + filtrado
print(neto)
