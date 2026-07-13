# main.py
# Punto de arranque del programa. Presenta un menú interactivo que permite
# registrar, listar y buscar productos y clientes del restaurante,
# creando los objetos a partir de los datos ingresados por el usuario.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def solicitar_datos_producto() -> Producto:
    """Solicita al usuario los datos necesarios para crear un Producto."""
    print("\n--- Registro de nuevo producto ---")
    nombre_ingresado = input("Nombre del producto: ")
    categoria_ingresada = input("Categoría (ej. Plato fuerte, Bebida, Postre): ")
    precio_ingresado = float(input("Precio: "))
    respuesta_disponible = input("¿Está disponible? (s/n): ").strip().lower()
    esta_disponible = respuesta_disponible == "s"

    return Producto(nombre_ingresado, categoria_ingresada, precio_ingresado, esta_disponible)


def solicitar_datos_cliente() -> Cliente:
    """Solicita al usuario los datos necesarios para crear un Cliente."""
    print("\n--- Registro de nuevo cliente ---")
    nombre_ingresado = input("Nombre completo: ")
    correo_ingresado = input("Correo electrónico: ")
    id_ingresado = input("ID del cliente: ")

    return Cliente(nombre_ingresado, correo_ingresado, id_ingresado)


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def main():
    # El restaurante se crea vacío; todos sus productos y clientes se
    # registran dinámicamente a partir del menú, no quedan quemados en el código.
    restaurante_actual = Restaurante("Sabor Andino")

    opcion_seleccionada = ""
    while opcion_seleccionada != "7":
        mostrar_menu()
        opcion_seleccionada = input("Seleccione una opción: ").strip()

        if opcion_seleccionada == "1":
            try:
                nuevo_producto = solicitar_datos_producto()
                restaurante_actual.registrar_producto(nuevo_producto)
            except ValueError as error:
                print(f"Error al registrar el producto: {error}")

        elif opcion_seleccionada == "2":
            restaurante_actual.listar_productos()

        elif opcion_seleccionada == "3":
            nombre_buscado = input("Ingrese el nombre del producto a buscar: ")
            restaurante_actual.buscar_producto(nombre_buscado)

        elif opcion_seleccionada == "4":
            nuevo_cliente = solicitar_datos_cliente()
            restaurante_actual.registrar_cliente(nuevo_cliente)

        elif opcion_seleccionada == "5":
            restaurante_actual.listar_clientes()

        elif opcion_seleccionada == "6":
            id_buscado = input("Ingrese el ID del cliente a buscar: ")
            restaurante_actual.buscar_cliente(id_buscado)

        elif opcion_seleccionada == "7":
            print("Saliendo del sistema. ¡Hasta pronto!")

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
