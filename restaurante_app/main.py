from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print(" 1. Registrar producto")
    print(" 2. Registrar bebida")
    print(" 3. Registrar cliente")
    print("----------------------------------------")
    print(" 4. Listar productos")
    print(" 5. Listar clientes")
    print("----------------------------------------")
    print(" 6. Salir")
    print("========================================")


def registrar_producto(servicio: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo: str = input("  Código: ").strip()
    nombre: str = input("  Nombre: ").strip()
    categoria: str = input("  Categoría: ").strip()
    precio: float = float(input("  Precio: ").strip())
    producto = Producto(codigo, nombre, categoria, precio)
    servicio.registrar_producto(producto)


def registrar_bebida(servicio: Restaurante) -> None:
    print("\n--- Registrar Bebida ---")
    codigo: str = input("  Código: ").strip()
    nombre: str = input("  Nombre: ").strip()
    categoria: str = input("  Categoría: ").strip()
    precio: float = float(input("  Precio: ").strip())
    tamano: str = input("  Tamaño (ej: 500ml, 1L): ").strip()
    tipo_envase: str = input("  Tipo de envase (ej: botella, lata, vaso): ").strip()
    bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
    servicio.registrar_producto(bebida)


def registrar_cliente(servicio: Restaurante) -> None:
    print("\n--- Registrar Cliente ---")
    identificacion: str = input("  Identificación: ").strip()
    nombre: str = input("  Nombre: ").strip()
    correo: str = input("  Correo: ").strip()
    cliente = Cliente(identificacion, nombre, correo)
    servicio.registrar_cliente(cliente)


def main() -> None:
    servicio = Restaurante()
    ejecutando: bool = True

    while ejecutando:
        mostrar_menu()
        opcion: str = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(servicio)
        elif opcion == "2":
            registrar_bebida(servicio)
        elif opcion == "3":
            registrar_cliente(servicio)
        elif opcion == "4":
            servicio.listar_productos()
        elif opcion == "5":
            servicio.listar_clientes()
        elif opcion == "6":
            print("\n  Hasta luego.\n")
            ejecutando = False
        else:
            print("  Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
