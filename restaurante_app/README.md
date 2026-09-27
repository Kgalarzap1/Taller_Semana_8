# Restaurante App - Semana 13

## Descripción

Proyecto correspondiente a la Semana 13 de la asignatura
Programación Orientada a Objetos.

En esta actividad se inicia la transición de restaurante_app
desde una aplicación basada en consola hacia una aplicación
con interfaz gráfica de usuario utilizando Tkinter.

El proyecto mantiene separadas las responsabilidades entre
modelos, servicios, datos e interfaz gráfica.

## Estructura del proyecto

restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py

## Responsabilidades

### Modelos

Producto representa los productos del restaurante y contiene
información como código, nombre, categoría, precio y stock.

Usuario representa los usuarios del sistema y contiene
identificación, nombre, correo, usuario y contraseña.

### Servicios

ArchivoServicio se encarga de leer la información almacenada
en los archivos JSON.

RestauranteServicio administra las colecciones de productos
y usuarios, reconstruye índices auxiliares, valida el acceso
y proporciona la información solicitada por las vistas.

### Datos

La carpeta datos contiene productos.json y usuarios.json.

Estos archivos almacenan la información local utilizada por
la aplicación.

### Interfaz gráfica

La carpeta ui contiene las vistas desarrolladas con Tkinter.

LoginView permite ingresar usuario y contraseña y solicita
la validación a RestauranteServicio.

MainView presenta el panel principal y permite visualizar
productos y usuarios registrados.

La opción Ventas se mantiene como funcionalidad pendiente
para una etapa posterior.

## Flujo de la aplicación

1. Se ejecuta main.py.
2. Se crea una única ventana principal de Tkinter.
3. Se preparan ArchivoServicio y RestauranteServicio.
4. Se muestra LoginView.
5. El usuario ingresa sus credenciales.
6. RestauranteServicio valida el acceso.
7. Si las credenciales son correctas se muestra MainView.
8. Desde MainView se pueden consultar productos y usuarios.
9. La opción Ventas muestra un mensaje de funcionalidad pendiente.
10. Cerrar sesión regresa a LoginView utilizando la misma ventana.

## Credenciales de prueba

Usuario: admin
Contraseña: 1234

También se puede utilizar:

Usuario: empleado
Contraseña: abcd

## Ejecución

Ubicarse dentro de la carpeta restaurante_app y ejecutar:

python main.py

## Funcionalidades implementadas

- Interfaz gráfica mediante Tkinter.
- Inicio de sesión simulado.
- Validación de campos vacíos.
- Validación de credenciales mediante RestauranteServicio.
- Lectura de archivos JSON mediante ArchivoServicio.
- Visualización de productos.
- Visualización de usuarios.
- Índices auxiliares para productos y usuarios.
- Cambio de vistas dentro de una única ventana.
- Cierre de sesión.

## Funcionalidades pendientes

La funcionalidad de ventas se incorporará posteriormente,
de acuerdo con la evolución del proyecto.