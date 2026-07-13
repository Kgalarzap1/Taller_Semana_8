# Sistema de Gestión de Restaurante - Semana 7

**Estudiante:** Kleber Galarza
**Asignatura:** Programación Orientada a Objetos
**Actividad:** Semana 7 - Taller Práctico - Constructores, decoradores y menú interactivo

## Descripción del sistema

Este proyecto evoluciona el sistema `restaurante_app` de la Semana 5, incorporando
constructores, decoradores de encapsulación (`@property` y `@setter`), la clase de
datos `@dataclass` y un menú interactivo de consola. Ahora los objetos `Producto`
y `Cliente` ya no se crean con valores fijos en el código, sino a partir de la
información que el usuario ingresa mediante `input()`.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase Producto: __init__, @property, @setter, validaciones
│   └── cliente.py       # Clase Cliente: implementada con @dataclass
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase Restaurante: registra, lista y busca productos/clientes
└── main.py               # Menú interactivo y punto de arranque del programa
```

## Uso del constructor en la clase Producto

`Producto` utiliza un constructor tradicional `__init__()` que recibe `nombre`,
`categoria`, `precio` y `disponible`. Dentro del constructor, cada atributo se
asigna a través de su respectivo *setter*, por lo que las validaciones se aplican
automáticamente desde el momento en que se crea el objeto.

## Uso de @property y @setter

Cada atributo principal de `Producto` (`nombre`, `categoria`, `precio`,
`disponible`) está protegido con `@property` (para lectura controlada) y
`@setter` (para escritura controlada con validaciones):
- El **nombre** no puede estar vacío.
- La **categoría** no puede estar vacía.
- El **precio** debe ser mayor que cero.

Si el usuario intenta ingresar un valor inválido, se lanza un `ValueError` que
es capturado en `main.py` para informar el error sin detener el programa.

## Uso de @dataclass en la clase Cliente

`Cliente` se implementa con el decorador `@dataclass`, el cual genera
automáticamente el constructor `__init__()` y otros métodos especiales a partir
de los atributos declarados (`nombre`, `correo`, `id_cliente`), evitando escribir
código repetitivo.

## Menú interactivo

`main.py` presenta un menú con 7 opciones (registrar/listar/buscar producto,
registrar/listar/buscar cliente, salir). Cada opción solicita los datos por
consola mediante `input()`, construye el objeto correspondiente y lo entrega
a la clase `Restaurante`, que se encarga de almacenarlo y de responder a las
consultas de listado o búsqueda.

## Cómo ejecutar el programa

```bash
cd restaurante_app
python3 main.py
```

## Reflexión

Crear objetos a partir de datos ingresados por el usuario, en lugar de dejarlos
fijos en el código, hace que el sistema sea realmente funcional y reutilizable:
el programa deja de ser una simple demostración y pasa a comportarse como una
aplicación real capaz de adaptarse a cualquier producto o cliente que se quiera
registrar. Además, combinar esto con `@property`, `@setter` y validaciones
asegura que, sin importar qué escriba el usuario, los objetos del sistema
siempre mantengan datos coherentes y válidos, evitando errores silenciosos más
adelante en el programa.
