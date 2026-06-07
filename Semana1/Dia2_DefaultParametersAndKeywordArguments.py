"""
# Parámetros por defecto
def calcular_cuota(monto, tasa_mensual=0.018, meses=12):
    #Calcula cuota mensual de un crédito (sistema francés).
    cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -meses)
    return round(cuota, 2)

# Llamadas distintas — todas válidas
print(calcular_cuota(5000000))           # usa defaults
print(calcular_cuota(5000000, meses=24)) # cambia solo los meses
print(calcular_cuota(                    # keyword args — muy legible
    monto=10000000,
    tasa_mensual=0.015,
    meses=36
))
"""
monto = int(input("Ingrese el monto que va a pedir prestado: "))
mes = int(input("Ingerese por cuantos meses va a sacar el crédito: "))

def calcular_cuota(monto, mes, tasa_mensual=0.018):
    """
        Calcula la cuota de un monto que se va a sacar prestado.

        Args:
            monto (float): Valor en COP prestado.
            mes (float): Tiempo en meses que se va a sacar el dinero.
            tasa (float): Tasa de interes. Default: 0.018.

        Returns:
            float: Cuota a pagar mensualmente, redondeado a 2 decimales.

    """
    cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -mes)
    return round(cuota, 2)

def calcular_credito(cuota, mes):
    """
            Calcula el dinero total a pagar por un monto prestado.

            Args:
                cuota (float): Cantidad a pagar mensualmente, redondeado a 2 decimales.
                mes (float): Meses que va a pagar el credito

            Returns:
                float: Pago total del credito, redondeado a 2 decimales.

    """
    credito = cuota * mes
    return round(credito, 2)

cuota = calcular_cuota(monto, mes, tasa_mensual=0.015)
total_credito = calcular_credito(cuota, mes)

print(f"Si saco prestado {monto} a {mes} meses, la cuota le queda en {cuota} y vas a pagar"
      f" en total {total_credito}")