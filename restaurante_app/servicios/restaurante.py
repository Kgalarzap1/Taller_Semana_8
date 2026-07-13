# restaurante.py
# Clase de servicio encargada de administrar las listas de productos
# y clientes registrados en el restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Gestiona el registro, listado y búsqueda de productos y clientes."""

    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []   # list[Producto]
        self.lista_clientes = []    # list[Cliente]

    # ---------- Productos ----------
    def registrar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto a la lista del restaurante."""
        self.lista_productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado correctamente.")

    def listar_productos(self) -> None:
        """Muestra en consola todos los productos registrados."""
        if not self.lista_productos:
            print("No hay productos registrados todavía.")
            return
        print(f"\n--- Productos de {self.nombre_restaurante} ---")
        for producto in self.lista_productos:
            print(producto.mostrar_informacion())

    def buscar_producto(self, nombre_buscado: str) -> None:
        """Busca un producto por nombre (sin distinguir mayúsculas/minúsculas)."""
        encontrados = [
            producto for producto in self.lista_productos
            if nombre_buscado.strip().lower() in producto.nombre.lower()
        ]
        if encontrados:
            print(f"\nResultados encontrados para '{nombre_buscado}':")
            for producto in encontrados:
                print(producto.mostrar_informacion())
        else:
            print(f"No se encontró ningún producto con el nombre '{nombre_buscado}'.")

    # ---------- Clientes ----------
    def registrar_cliente(self, cliente: Cliente) -> None:
        """Agrega un nuevo cliente a la lista del restaurante."""
        self.lista_clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado correctamente.")

    def listar_clientes(self) -> None:
        """Muestra en consola todos los clientes registrados."""
        if not self.lista_clientes:
            print("No hay clientes registrados todavía.")
            return
        print(f"\n--- Clientes de {self.nombre_restaurante} ---")
        for cliente in self.lista_clientes:
            print(cliente.mostrar_informacion())

    def buscar_cliente(self, id_buscado: str) -> None:
        """Busca un cliente por su id_cliente."""
        encontrado = next(
            (cliente for cliente in self.lista_clientes if cliente.id_cliente == id_buscado),
            None
        )
        if encontrado:
            print(f"\nCliente encontrado:")
            print(encontrado.mostrar_informacion())
        else:
            print(f"No se encontró ningún cliente con el ID '{id_buscado}'.")
