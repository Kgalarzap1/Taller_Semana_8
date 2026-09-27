import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ) -> None:

        super().__init__(
            master,
            bg="#f5f5f5"
        )

        self.restaurante_servicio = (
            restaurante_servicio
        )

        self.usuario_actual = (
            usuario_actual
        )

        self.al_cerrar_sesion = (
            al_cerrar_sesion
        )

        self.contenido = None

        self.construir_interfaz()

    def construir_interfaz(self) -> None:

        encabezado = tk.Frame(
            self,
            bg="#263238",
            padx=25,
            pady=15
        )

        encabezado.pack(
            fill="x"
        )

        tk.Label(
            encabezado,
            text="RESTAURANTE APP",
            bg="#263238",
            fg="white",
            font=("Arial", 19, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            encabezado,
            text=(
                f"Bienvenido, "
                f"{self.usuario_actual.nombre}"
            ),
            bg="#263238",
            fg="white",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        barra_menu = tk.Frame(
            self,
            bg="#dddddd",
            padx=15,
            pady=10
        )

        barra_menu.pack(
            fill="x"
        )

        ttk.Button(
            barra_menu,
            text="Productos",
            command=self.mostrar_productos
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            barra_menu,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            barra_menu,
            text="Ventas",
            command=(
                self.mostrar_funcionalidad_pendiente
            )
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            barra_menu,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(
            side="right",
            padx=5
        )

        self.contenido = tk.Frame(
            self,
            bg="#f5f5f5",
            padx=25,
            pady=20
        )

        self.contenido.pack(
            fill="both",
            expand=True
        )

        self.mostrar_inicio()

    def limpiar_contenido(self) -> None:

        for elemento in (
            self.contenido.winfo_children()
        ):
            elemento.destroy()

    def mostrar_inicio(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg="#f5f5f5",
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        tk.Label(
            self.contenido,
            text=(
                "Seleccione una opción para "
                "consultar la información."
            ),
            bg="#f5f5f5",
            font=("Arial", 11)
        ).pack(
            anchor="w"
        )

        resumen = (
            f"Productos registrados: "
            f"{self.restaurante_servicio.cantidad_productos()}"
            f"   |   "
            f"Usuarios registrados: "
            f"{self.restaurante_servicio.cantidad_usuarios()}"
        )

        tk.Label(
            self.contenido,
            text=resumen,
            bg="#f5f5f5",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=(15, 0)
        )

    def mostrar_productos(self) -> None:

        self.limpiar_contenido()

        self.crear_titulo(
            "Productos registrados"
        )

        productos = (
            self.restaurante_servicio
            .listar_productos()
        )

        if not productos:

            self.crear_fila(
                "No existen productos registrados."
            )

            return

        for producto in productos:

            texto = (
                f"{producto.codigo} | "
                f"{producto.nombre} | "
                f"{producto.categoria} | "
                f"${producto.precio:.2f} | "
                f"Stock: {producto.stock}"
            )

            self.crear_fila(texto)

    def mostrar_usuarios(self) -> None:

        self.limpiar_contenido()

        self.crear_titulo(
            "Usuarios registrados"
        )

        usuarios = (
            self.restaurante_servicio
            .listar_usuarios()
        )

        if not usuarios:

            self.crear_fila(
                "No existen usuarios registrados."
            )

            return

        for usuario in usuarios:

            texto = (
                f"{usuario.identificacion} | "
                f"{usuario.nombre} | "
                f"{usuario.correo} | "
                f"Usuario: {usuario.usuario}"
            )

            self.crear_fila(texto)

    def crear_titulo(
        self,
        texto: str
    ) -> None:

        tk.Label(
            self.contenido,
            text=texto,
            bg="#f5f5f5",
            font=("Arial", 17, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

    def crear_fila(
        self,
        texto: str
    ) -> None:

        fila = tk.Frame(
            self.contenido,
            bg="white",
            padx=12,
            pady=10
        )

        fila.pack(
            fill="x",
            pady=4
        )

        tk.Label(
            fila,
            text=texto,
            bg="white",
            font=("Arial", 10)
        ).pack(
            anchor="w"
        )

    def mostrar_funcionalidad_pendiente(
        self
    ) -> None:

        messagebox.showinfo(
            "Próximamente",
            (
                "La funcionalidad de ventas "
                "será incorporada posteriormente."
            )
        )

    def cerrar_sesion(self) -> None:

        self.al_cerrar_sesion()