from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(
        self,
        archivo_servicio: ArchivoServicio
    ) -> None:

        self.archivo_servicio = archivo_servicio

        # Colecciones principales
        self._productos: list[Producto] = (
            self.archivo_servicio.cargar_productos()
        )

        self._usuarios: list[Usuario] = (
            self.archivo_servicio.cargar_usuarios()
        )

        # Índices auxiliares
        self._indice_productos: dict[
            str, Producto
        ] = {}

        self._indice_usuarios: dict[
            str, Usuario
        ] = {}

        self._indice_acceso: dict[
            str, Usuario
        ] = {}

        self._reconstruir_indices()

    def _reconstruir_indices(self) -> None:
        """
        Reconstruye los índices a partir de las
        colecciones cargadas desde los archivos JSON.
        """

        self._indice_productos = {
            producto.codigo: producto
            for producto in self._productos
        }

        self._indice_usuarios = {
            usuario.identificacion: usuario
            for usuario in self._usuarios
        }

        self._indice_acceso = {
            usuario.usuario: usuario
            for usuario in self._usuarios
        }

    def validar_acceso(
        self,
        nombre_usuario: str,
        contrasena: str
    ) -> Usuario | None:
        """
        Valida el acceso utilizando el índice de usuarios.
        """

        usuario = self._indice_acceso.get(
            nombre_usuario
        )

        if usuario is None:
            return None

        if usuario.contrasena != contrasena:
            return None

        return usuario

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        return self._indice_productos.get(codigo)

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        return self._indice_usuarios.get(
            identificacion
        )

    def listar_productos(
        self
    ) -> list[Producto]:

        return self._productos

    def listar_usuarios(
        self
    ) -> list[Usuario]:

        return self._usuarios

    def cantidad_productos(self) -> int:

        return len(self._productos)

    def cantidad_usuarios(self) -> int:

        return len(self._usuarios)