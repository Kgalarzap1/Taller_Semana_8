# producto.py
# Clase que representa un producto del restaurante.
# Aplica constructor tradicional __init__, además de @property y @setter
# para controlar el acceso y la modificación de sus atributos.


class Producto:
    """Representa un producto (plato o bebida) disponible en el restaurante."""

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool):
        # Se usan los setters dentro del constructor para que las validaciones
        # se apliquen también al momento de crear el objeto.
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # ---------- Propiedad: nombre ----------
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = nuevo_nombre.strip()

    # ---------- Propiedad: categoria ----------
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str) -> None:
        if not nueva_categoria or not nueva_categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = nueva_categoria.strip()

    # ---------- Propiedad: precio ----------
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = nuevo_precio

    # ---------- Propiedad: disponible ----------
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, esta_disponible: bool) -> None:
        self._disponible = esta_disponible

    def mostrar_informacion(self) -> str:
        """Devuelve la información del producto en un formato legible."""
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"Nombre: {self.nombre} | Categoría: {self.categoria} | "
                f"Precio: ${self.precio:.2f} | Estado: {estado}")

    def __str__(self) -> str:
        return self.mostrar_informacion()
