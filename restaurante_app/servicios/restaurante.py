"""Clase de servicio encargada de administrar productos y clientes."""


class Restaurante:
    """Servicio principal del sistema: guarda y consulta productos y clientes."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # ---------- Productos ----------
    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, nombre):
        nombre_buscado = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscado:
                return producto
        return None

    # ---------- Clientes ----------
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, id_cliente):
        id_buscado = id_cliente.strip().lower()
        for cliente in self.clientes:
            if cliente.id_cliente.strip().lower() == id_buscado:
                return cliente
        return None
