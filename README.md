# Sistema de Gestión de Restaurante — Semana 7 (POO)

- **Estudiante:** Leython Josue Hidalgo Valdez
- **Asignatura:** Programación Orientada a Objetos
- **Tema:** Aplicación de constructores, decoradores y menú interactivo en un proyecto Python modular

## Descripción del sistema

Este proyecto es una evolución del sistema `restaurante_app` desarrollado para
la Semana 7 de la asignatura Programación Orientada a Objetos. Permite
registrar, listar y buscar **productos** y **clientes** de un restaurante a
través de un menú interactivo ejecutado desde consola. A diferencia de
entregas anteriores, los objetos ya no están escritos directamente en el
código: se crean a partir de la información que el usuario ingresa mediante
`input()`.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

- **modelos/producto.py**: contiene la clase `Producto`.
- **modelos/cliente.py**: contiene la clase `Cliente`.
- **servicios/restaurante.py**: contiene la clase de servicio `Restaurante`,
  encargada de administrar las listas de productos y clientes.
- **main.py**: punto de arranque del programa; muestra el menú, pide los
  datos al usuario y llama a los métodos del servicio.

## Constructor en la clase Producto

`Producto` se implementa con un constructor tradicional `__init__`, que
recibe `nombre`, `categoria`, `precio` y `disponible`. Dentro del
constructor, cada atributo se asigna a través de su respectivo setter, de
modo que las validaciones se aplican también en el momento de crear el
objeto.

## Uso de @property y @setter

Los atributos `nombre`, `categoria`, `precio` y `disponible` de `Producto`
están controlados mediante `@property` y su correspondiente `@setter`. Los
setters validan que el nombre y la categoría no estén vacíos y que el precio
sea mayor que cero; si alguna validación falla, se lanza un `ValueError` que
el menú captura para informar al usuario sin detener el programa.

## Uso de @dataclass en la clase Cliente

`Cliente` se implementa con el decorador `@dataclass`, ya que representa un
conjunto de datos simples (`nombre`, `correo`, `id_cliente`) sin necesidad de
validaciones adicionales. El decorador genera automáticamente el
constructor y otros métodos básicos de la clase.

## Descripción del menú interactivo

Al ejecutar `main.py` se muestra un menú con las siguientes opciones:

```
1. Registrar producto
2. Listar productos
3. Buscar producto
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
7. Salir
```

Cada opción solicita los datos necesarios mediante `input()`, crea el objeto
correspondiente (`Producto` o `Cliente`) y lo pasa a la clase de servicio
`Restaurante`, que se encarga de guardarlo, listarlo o buscarlo. El programa
se mantiene en ejecución hasta que el usuario elige la opción 7.

## Reflexión

Construir los objetos a partir de datos ingresados por el usuario, en lugar
de dejarlos escritos directamente en el código, obliga a pensar en las
validaciones desde el diseño de la clase y no como un detalle posterior.
Además, separar el modelo (`Producto`, `Cliente`) del servicio (`Restaurante`)
deja más claro qué parte del sistema es responsable de crear datos válidos y
cuál es responsable de administrarlos, lo que hace el proyecto más fácil de
mantener y de ampliar a futuro.
