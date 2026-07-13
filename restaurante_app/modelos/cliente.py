# cliente.py
# Clase que representa a un cliente del restaurante.
# Se implementa utilizando el decorador @dataclass, el cual genera
# automáticamente el constructor y otros métodos especiales.

from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa a un cliente registrado en el restaurante."""
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self) -> str:
        """Devuelve la información del cliente en un formato legible."""
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"
