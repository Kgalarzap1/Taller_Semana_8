class Cliente:
    """Clase que representa a un cliente registrado en el restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> None:
        print(f"  [Cliente]  ID: {self.identificacion} | Nombre: {self.nombre} "
              f"| Correo: {self.correo}")
