# Archivo clientes.py

import json

ARCHIVO_CLIENTES = 'clientes.json'

class Cliente:
    def __init__(self, nombre, contrasena, direccion, correo):
        self.nombre, self.contrasena, self.direccion, self.correo = nombre, contrasena, direccion, correo

    def __str__(self):
        return f"Cliente: {self.nombre}\nDirección: {self.direccion}\nCorreo: {self.correo}"

class ManejadorClientes:
    def __init__(self):
        self.base_de_datos = self.cargar_base_datos()

    def cargar_base_datos(self):
        try:
            with open(ARCHIVO_CLIENTES, 'r') as archivo_json:
                return {nombre: Cliente(nombre, contrasena, direccion, correo) for nombre, (contrasena, direccion, correo) in json.load(archivo_json).items()}
        except FileNotFoundError:
            return {}

    def guardar_base_datos(self):
        with open(ARCHIVO_CLIENTES, 'w') as archivo_json:
            json.dump({nombre: (cliente.contrasena, cliente.direccion, cliente.correo) for nombre, cliente in self.base_de_datos.items()}, archivo_json, indent=2)

    def validar_correo(self, correo):
        return '@' in correo

    def registrar_cliente(self):
        nombre = input("Ingrese nombre de cliente: ")
        contrasena = input("Ingrese contraseña: ")
        direccion = input("Ingrese dirección: ")
        
        # Validar el correo electrónico
        while True:
            correo = input("Ingrese correo electrónico: ")
            if self.validar_correo(correo):
                break
            print("La dirección de correo no es válida. Debe contener '@'.")
            
        self.base_de_datos[nombre] = Cliente(nombre, contrasena, direccion, correo)
        print(f"Cliente '{nombre}' registrado exitosamente.")

    def mostrar_clientes(self):
        print("\nClientes registrados:")
        for cliente in self.base_de_datos.values():
            print(cliente)

def main():
    manejador_clientes = ManejadorClientes()

    while True:
        print("\n1. Registrar nuevo cliente")
        print("2. Mostrar clientes registrados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            manejador_clientes.registrar_cliente()
        elif opcion == '2':
            manejador_clientes.mostrar_clientes()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            manejador_clientes.guardar_base_datos()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
