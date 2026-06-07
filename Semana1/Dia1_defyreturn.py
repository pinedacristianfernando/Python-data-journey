"""
# Función con print — no puedes usar el resultado
def convertir_mal(cop):
    print(cop / 4200)  # Solo muestra, no devuelve nada

resultado = convertir_mal(100000)
print(resultado)  # → None  (¡no hay valor!)

# Función con return — puedes usar el resultado
def convertir_cop_usd(cop, tasa=4200):
    return cop / tasa

precio_usd = convertir_cop_usd(100000)
print(f"${precio_usd:.2f} USD")  # → $23.81 USD

# Ahora puedes usar el resultado en otros cálculos
con_impuesto = convertir_cop_usd(100000) * 1.19
print(f"Con IVA: ${con_impuesto:.2f} USD")  # → $28.33 USD
"""

monto = int(input("Ingrese el monto en COP: "))
def cop_a_usd(monto_cop,tasa=4200):
    """
    Convierte un monto de pesos colombianos a dólares.

    Args:
        monto (float): Valor en COP a convertir.
        tasa (float): Tasa de cambio COP/USD. Default: 4200.

    Returns:
        float: Equivalente en USD, redondeado a 2 decimales.

    """
    return round(monto_cop / tasa,2)
print(f"El monto {monto} a USD es {cop_a_usd(monto)}")