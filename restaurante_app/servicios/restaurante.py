from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio principal que administra productos y clientes del restaurante."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto o bebida. Retorna False si el código ya existe."""
        for p in self._productos:
            if p.codigo == producto.codigo:
                print(f"  ⚠ Ya existe un producto con el código '{producto.codigo}'.")
                return False
        self._productos.append(producto)
        print(f"  ✔ Producto '{producto.nombre}' registrado correctamente.")
        return True

    def listar_productos(self) -> None:
        """Lista todos los productos y bebidas usando polimorfismo."""
        if not self._productos:
            print("  No hay productos registrados.")
            return
        print(f"\n  {'─' * 60}")
        print(f"  PRODUCTOS REGISTRADOS ({len(self._productos)})")
        print(f"  {'─' * 60}")
        for producto in self._productos:
            producto.mostrar_informacion()
        print(f"  {'─' * 60}")

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente. Retorna False si la identificación ya existe."""
        for c in self._clientes:
            if c.identificacion == cliente.identificacion:
                print(f"  ⚠ Ya existe un cliente con la identificación '{cliente.identificacion}'.")
                return False
        self._clientes.append(cliente)
        print(f"  ✔ Cliente '{cliente.nombre}' registrado correctamente.")
        return True

    def listar_clientes(self) -> None:
        """Lista todos los clientes registrados."""
        if not self._clientes:
            print("  No hay clientes registrados.")
            return
        print(f"\n  {'─' * 60}")
        print(f"  CLIENTES REGISTRADOS ({len(self._clientes)})")
        print(f"  {'─' * 60}")
        for cliente in self._clientes:
            cliente.mostrar_informacion()
        print(f"  {'─' * 60}")
