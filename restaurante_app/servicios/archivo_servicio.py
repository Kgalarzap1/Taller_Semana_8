import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:

    def __init__(self, carpeta_datos) -> None:

        self.carpeta_datos = Path(carpeta_datos)

        self.ruta_productos = (
            self.carpeta_datos / "productos.json"
        )

        self.ruta_usuarios = (
            self.carpeta_datos / "usuarios.json"
        )

    def cargar_productos(self) -> list[Producto]:

        try:
            with self.ruta_productos.open(
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos = []

            for dato in datos:

                producto = Producto(
                    dato["codigo"],
                    dato["nombre"],
                    dato["categoria"],
                    float(dato["precio"]),
                    int(dato["stock"])
                )

                productos.append(producto)

            return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json "
                "contiene un JSON inválido."
            )
            return []

        except (KeyError, ValueError, TypeError) as error:
            print(
                f"Error al cargar productos: {error}"
            )
            return []

    def cargar_usuarios(self) -> list[Usuario]:

        try:
            with self.ruta_usuarios.open(
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            usuarios = []

            for dato in datos:

                usuario = Usuario(
                    dato["identificacion"],
                    dato["nombre"],
                    dato["correo"],
                    dato["usuario"],
                    dato["contrasena"]
                )

                usuarios.append(usuario)

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: usuarios.json "
                "contiene un JSON inválido."
            )
            return []

        except (KeyError, ValueError, TypeError) as error:
            print(
                f"Error al cargar usuarios: {error}"
            )
            return []