

import json

ARCHIVO_PRODUCTOS = 'productos.json'

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre, self.precio, self.stock = nombre, precio, stock

    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio}\nStock: {self.stock}"

class ManejadorProductos:
    def __init__(self):
        self.base_de_datos = self.cargar_base_datos()

    def cargar_base_datos(self):
        try:
            with open(ARCHIVO_PRODUCTOS, 'r') as archivo_json:
                return {nombre: Producto(nombre, precio, stock) for nombre, (precio, stock) in json.load(archivo_json).items()}
        except FileNotFoundError:
            return {}

    def guardar_base_datos(self):
        with open(ARCHIVO_PRODUCTOS, 'w') as archivo_json:
            json.dump({nombre: (producto.precio, producto.stock) for nombre, producto in self.base_de_datos.items()}, archivo_json, indent=2)

    def registrar_producto(self):
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input("Ingrese precio del producto: "))
        stock = int(input("Ingrese stock del producto: "))

        self.base_de_datos[nombre] = Producto(nombre, precio, stock)
        print(f"Producto '{nombre}' registrado exitosamente.")

    def mostrar_productos(self):
        print("\nProductos registrados:")
        for producto in self.base_de_datos.values():
            print(producto)

def main():
    manejador_productos = ManejadorProductos()

    while True:
        print("\n1. Registrar nuevo producto")
        print("2. Mostrar productos registrados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            manejador_productos.registrar_producto()
        elif opcion == '2':
            manejador_productos.mostrar_productos()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            manejador_productos.guardar_base_datos()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
