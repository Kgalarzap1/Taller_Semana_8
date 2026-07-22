# restaurante_app

**Estudiante:** Kleber Alexander Galarza Badillo  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 8 — Organización modular con principios SOLID

---

## Descripción del sistema

Sistema de gestión básica para un restaurante que permite registrar y listar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola. El proyecto aplica los principios SOLID de responsabilidad única, abierto/cerrado y sustitución de Liskov.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

---

## Responsabilidad de cada clase

| Clase | Archivo | Responsabilidad |
|---|---|---|
| `Producto` | `modelos/producto.py` | Representa los datos comunes de un producto del restaurante |
| `Bebida` | `modelos/bebida.py` | Especialización de Producto con atributos de tamaño y tipo de envase |
| `Cliente` | `modelos/cliente.py` | Representa la información de un cliente registrado |
| `Restaurante` | `servicios/restaurante.py` | Administra las colecciones y operaciones del sistema |
| `main.py` | — | Coordina la interacción por consola y el flujo del programa |

---

## Relación entre Producto y Bebida

`Bebida` hereda de `Producto` porque una bebida **es un tipo de producto** del restaurante. Esta relación permite almacenar ambos tipos en una misma lista de productos y ejecutar el método `mostrar_informacion()` de forma polimórfica, sin necesidad de verificar el tipo de cada objeto durante el listado.

---

## Principios SOLID aplicados

### S — Responsabilidad Única (SRP)
Cada clase tiene una única razón para cambiar: `Producto` y `Bebida` representan entidades, `Cliente` representa un cliente, `Restaurante` administra las colecciones, y `main.py` maneja exclusivamente la interacción con el usuario.

### O — Abierto/Cerrado (OCP)
El sistema está abierto a la extensión: la clase `Bebida` amplió el sistema añadiendo atributos propios y sobrescribiendo `mostrar_informacion()` sin modificar la lógica del servicio `Restaurante`.

### L — Sustitución de Liskov (LSP)
Un objeto `Bebida` puede utilizarse en cualquier lugar donde se espere un `Producto`, ya que hereda y respeta su comportamiento. La lista `_productos` acepta objetos de ambas clases sin condiciones especiales.

---

## Instrucciones de ejecución

```bash
# Clonar el repositorio
git clone https://github.com/Kgalarzap1/restaurante_app.git
cd restaurante_app

# Ejecutar desde la carpeta raíz del proyecto
python restaurante_app/main.py
```

> **Nota:** ejecutar desde la raíz del repositorio para que los imports relativos funcionen correctamente.

---

## Reflexión

Diseñar proyectos con responsabilidades bien definidas permite que cada parte del sistema pueda modificarse o extenderse sin afectar al resto. En este proyecto, agregar una nueva categoría de producto (como `Postre`) solo requeriría crear una nueva clase hija de `Producto`, sin tocar el servicio ni el menú. Esa capacidad de crecer sin romper lo existente es la diferencia entre un código mantenible y uno frágil.
