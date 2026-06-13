"""
# *args → recibe cualquier cantidad de salarios
def promedio_salarios(*salarios):
    if not salarios:
        return 0
    return sum(salarios) / len(salarios)

print(promedio_salarios(2500000, 3200000, 4100000))  # 3 salarios
print(promedio_salarios(1800000))                    # 1 salario

# **kwargs → describe un producto con campos variables
def describir_producto(nombre, **detalles):
    print(f"\nProducto: {nombre}")
    for campo, valor in detalles.items():
        print(f"  {campo}: {valor}")

describir_producto(
    "Laptop",
    marca="Lenovo",
    ram="16GB",
    precio_cop=3500000,
    disponible=True
)
"""

"""
Parte 1: función promedio_variable(*numeros) que calcule el promedio de cualquier cantidad de números 
y maneje el caso de lista vacía. Parte 2: función ficha_empleado(nombre, **datos) que reciba nombre y 
cualquier cantidad de datos adicionales (cargo, salario, ciudad, etc.) e imprima una ficha formateada.
"""

def promedio_variable(*numeros):
    """
        Calcula el promedio de los numeros ingresados.

        Args:
            numeros (list): Valores numericos que se ingresan.

        Returns:
            list: Promedio de los numeros ingresados.

    """
    return sum(numeros) / len(numeros)
print(promedio_variable(500,200,500,300))

def informacion_cliente(nombre, **detalles):
    """
        Ingresar cantiad indefinida informacion de cliente.

        Args:
            nombre, detalles (dict): Informacion del cliente, clave y valor respectivamente.

        Returns:
            dict: Informacion del cliente.

    """
    print(f"\nCliente: {nombre}")
    for campo, valor in detalles.items():
        print(f"  {campo}: {valor}")
informacion_cliente("Juan",
                    Apellido="Perez",
                    Cuidad="Bogota",
                    Compra="Carro")
