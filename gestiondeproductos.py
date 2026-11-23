import json
from pathlib import Path

# El archivo se crea en la misma carpeta que este programa.
ARCHIVO_PRODUCTOS = Path("productos.json")


def cargar_productos():
    """Recupera los productos guardados al iniciar el programa."""
    if not ARCHIVO_PRODUCTOS.exists():
        return []

    try:
        with ARCHIVO_PRODUCTOS.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
        if isinstance(productos, list) and all(isinstance(p, str) for p in productos):
            return productos
        print("⚠️ El archivo de productos no tiene el formato esperado. Se usará una lista vacía.")
    except (OSError, json.JSONDecodeError):
        print("⚠️ No se pudo leer productos.json. Se usará una lista vacía.")
    return []


def guardar_productos(productos):
    """Guarda la lista para que los cambios persistan al cerrar el programa."""
    try:
        with ARCHIVO_PRODUCTOS.open("w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, ensure_ascii=False, indent=4)
        return True
    except OSError as error:
        print(f"⚠️ No se pudieron guardar los productos: {error}")
        return False


def agregar_producto(productos):
    print("\n--- AGREGAR PRODUCTO ---")
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("⚠️ Error: El nombre del producto no puede estar vacío.")

    productos.append(nombre)
    if guardar_productos(productos):
        print(f"✅ El producto '{nombre}' fue agregado correctamente.")
    else:
        productos.pop()  # Deshacer el cambio si no se pudo guardar.
        print("❌ No se agregó el producto porque no pudo guardarse.")


def mostrar_productos(productos):
    print("\n--- LISTA DE PRODUCTOS ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Productos registrados:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto}")


def buscar_producto(productos):
    print("\n--- BUSCAR UN PRODUCTO ---")
    if not productos:
        print("La lista está vacía. No hay productos para buscar.")
        return

    busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
    if not busqueda:
        print("⚠️ Error: Debe ingresar un nombre válido.")
        return

    for producto in productos:
        if producto.lower() == busqueda.lower():
            print(f"✅ El producto '{producto}' SÍ está en la lista.")
            return
    print(f"❌ El producto '{busqueda}' NO está en la lista.")


def eliminar_producto(productos):
    print("\n--- ELIMINAR UN PRODUCTO ---")
    if not productos:
        print("La lista está vacía. No hay productos para eliminar.")
        return

    nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()
    if not nombre:
        print("⚠️ Error: Debe ingresar un nombre válido.")
        return

    for producto in productos:
        if producto.lower() == nombre.lower():
            posicion = productos.index(producto)
            productos.remove(producto)
            if guardar_productos(productos):
                print(f"✅ El producto '{producto}' fue eliminado correctamente.")
            else:
                productos.insert(posicion, producto)  # Deshacer el cambio.
                print("❌ No se eliminó el producto porque no pudo guardarse.")
            return
    print(f"⚠️ Error: El producto '{nombre}' no existe en la lista.")


def gestor_de_productos():
    productos = cargar_productos()

    while True:
        print("\n========================================")
        print("    GESTOR DE PRODUCTOS INTERACTIVO     ")
        print("========================================")
        print("1. Agregar producto")
        print("2. Mostrar lista de productos")
        print("3. Buscar un producto")
        print("4. Eliminar un producto")
        print("5. Salir")
        print("========================================")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("\n¡Gracias por utilizar el Gestor de Productos! Hasta luego.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    gestor_de_productos()
