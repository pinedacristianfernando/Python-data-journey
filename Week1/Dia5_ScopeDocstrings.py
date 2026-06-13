# Scope — ejemplo de qué evitar y qué hacer
tasa = 4200  # variable global

# Evitar — usa la global directamente
def convertir_mal(monto):
    return monto / tasa  # depende de algo externo

# Mejor — la tasa entra como parámetro
def convertir_cop_usd(monto, tasa=4200):
    """
    Convierte un monto de pesos colombianos a dólares.

    Args:
        monto (float): Valor en COP a convertir.
        tasa (float): Tasa de cambio COP/USD. Default: 4200.

    Returns:
        float: Equivalente en USD, redondeado a 2 decimales.
    """
    return round(monto / tasa, 2)

# Ver el docstring en acción
help(convertir_cop_usd)