"""Punto de arranque del sistema de restaurante."""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")


def registrar_producto(restaurante):
    print("\n--- Registro de producto ---")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("El precio ingresado no es válido.")
        return

    disponible_texto = input("¿Disponible? (s/n): ").strip().lower()
    disponible = disponible_texto == "s"

    # La creación del objeto pasa por el constructor, que a su vez
    # dispara las validaciones definidas en los setters de Producto.
    try:
        producto = Producto(nombre, categoria, precio, disponible)
    except ValueError as error:
        print(f"No se pudo registrar el producto: {error}")
        return

    restaurante.registrar_producto(producto)
    print("Producto registrado correctamente.")


def listar_productos(restaurante):
    print("\n--- Productos registrados ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados todavía.")
        return
    for producto in productos:
        print(producto.mostrar_informacion())


def buscar_producto(restaurante):
    print("\n--- Búsqueda de producto ---")
    nombre = input("Nombre del producto a buscar: ")
    producto = restaurante.buscar_producto(nombre)
    if producto:
        print(producto.mostrar_informacion())
    else:
        print("No se encontró un producto con ese nombre.")


def registrar_cliente(restaurante):
    print("\n--- Registro de cliente ---")
    nombre = input("Nombre del cliente: ")
    correo = input("Correo: ")
    id_cliente = input("ID del cliente: ")

    # Cliente es un dataclass, por lo que el constructor se genera
    # automáticamente a partir de los atributos declarados en el modelo.
    cliente = Cliente(nombre, correo, id_cliente)
    restaurante.registrar_cliente(cliente)
    print("Cliente registrado correctamente.")


def listar_clientes(restaurante):
    print("\n--- Clientes registrados ---")
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados todavía.")
        return
    for cliente in clientes:
        print(cliente.mostrar_informacion())


def buscar_cliente(restaurante):
    print("\n--- Búsqueda de cliente ---")
    id_cliente = input("ID del cliente a buscar: ")
    cliente = restaurante.buscar_cliente(id_cliente)
    if cliente:
        print(cliente.mostrar_informacion())
    else:
        print("No se encontró un cliente con ese ID.")


def main():
    # El restaurante inicia vacío; todos los productos y clientes se
    # crean a partir de lo que el usuario ingresa por consola.
    restaurante = Restaurante("Restaurante El Buen Sabor")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()
