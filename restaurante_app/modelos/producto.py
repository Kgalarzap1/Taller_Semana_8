class Producto:
    """Clase base que representa un producto general del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> None:
        print(f"  [Producto] Código: {self.codigo} | Nombre: {self.nombre} "
              f"| Categoría: {self.categoria} | Precio: ${self.precio:.2f}")
