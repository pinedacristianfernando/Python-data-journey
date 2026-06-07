"""
calculadora_financiera
"""

# 1. cop_a_usd(monto, tasa=4200)      ← Día 1
def cop_a_usd(monto_cop,tasa=4200):
    """
    Convierte un monto de pesos colombianos a dólares.

    Args:
        monto_cop (float): Valor en COP a convertir.
        tasa (float): Tasa de cambio COP/USD. Default: 4200.

    Returns:
        float: Equivalente en USD, redondeado a 2 decimales.

    """
    return round(monto_cop / tasa,2)

# 2. calcular_cuota(monto, tasa, meses) ← Día 2
def calcular_cuota(monto, mes, tasa_mensual=0.018):
    """
        Calcula la cuota de un monto que se va a sacar prestado.

        Args:
            monto (float): Valor en COP prestado.
            mes (float): Tiempo en meses que se va a sacar el dinero.
            tasa_mensual (float): Tasa de interes. Default: 0.018.

        Returns:
            float: Cuota a pagar mensualmente, redondeado a 2 decimales.

    """
    cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -mes)
    return round(cuota, 2)

# 4. retencion = lambda s: ...         ← Día 4
def calcular_retencion (salario_usd,tasa_ret=0.04):
    """
    Calcula la tasa de retencion si el salario.

    Args:
        salario_usd (float): Valor en USD a calcular la retencion.
        tasa_ret (float): Valor retenido del salario si el salario es mayor a 750 USD. Default: 0.04.

    Returns:
        float: Valores retenidos si se cumple la condicion.
    """
    return round(salario_usd * tasa_ret,2) if salario_usd > 750 else 0

def resumen_empleado(nombre, **datos):
    """
    Recibe nombre y datos variables del empleado.
    Imprime un resumen financiero completo usando
    las funciones anteriores.
    """
    salario = datos.get("salario_cop", 0)
    meses = datos.get("meses_credito", 0)
    prestamo = datos.get("prestamo_usd", 0)

    salario_usd = cop_a_usd(salario)
    retenido = calcular_retencion(salario_usd, tasa_ret=0.04)
    cuota = calcular_cuota(prestamo, meses)
    neto = cop_a_usd(salario)-retenido-cuota

    print(f"\n=== Resumen financiero: {nombre} ===")
    print(f"Salario COP:     ${salario:,.0f}")
    print(f"Salario USD:     ${salario_usd:,.2f}")
    print(f"Retención 4% USD:    ${retenido:,.2f}")
    print(f"Cuota crédito USD:   ${cuota:,.2f}")
    print(f"Final neto USD:      ${neto:,.2f}")

empleados = [
    {
        "nombre": "Felipe",
        "salario_cop": 10000000,
        "meses_credito": 12,
        "prestamo_usd": 5000,
    },
    {
        "nombre": "Laura",
        "salario_cop": 4200000,
        "meses_credito": 24,
        "prestamo_usd": 2000,
    },
    {
        "nombre": "Carlos",
        "salario_cop": 7500000,
        "meses_credito": 6,
        "prestamo_usd": 1000,
    },
]

for empleado in empleados:
    resumen_empleado(**empleado)



