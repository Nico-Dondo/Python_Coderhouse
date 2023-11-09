import json

ARCHIVO_BASE_DATOS = 'clientes.json'

class Cliente:
    def __init__(self, nombre, contrasena, direccion, correo):
        self.nombre = nombre
        self.contrasena = contrasena
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return f"Cliente: {self.nombre}\nDirección: {self.direccion}\nCorreo: {self.correo}"

class ManejadorClientes:
    def __init__(self):
        self.base_de_datos = self.cargar_base_datos()

    def cargar_base_datos(self):
        try:
            with open(ARCHIVO_BASE_DATOS, 'r') as archivo:
                datos = json.load(archivo)
                return {nombre: Cliente(nombre, contrasena, direccion, correo) for nombre, (contrasena, direccion, correo) in datos.items()}
        except FileNotFoundError:
            return {}

    def guardar_base_datos(self):
        with open(ARCHIVO_BASE_DATOS, 'w') as archivo:
            datos = {cliente.nombre: (cliente.contrasena, cliente.direccion, cliente.correo) for cliente in self.base_de_datos.values()}
            json.dump(datos, archivo, indent=2)

    def validar_correo(self, correo):
        return '@' in correo

    def registrar_cliente(self):
        nombre_cliente = input("Ingrese nombre de cliente: ")

        if nombre_cliente in self.base_de_datos:
            print("El cliente ya existe. Por favor, elija otro nombre de cliente.")
        else:
            contrasena = input("Ingrese contraseña: ")
            direccion = input("Ingrese dirección: ")
            
        
            correo_valido = False
            while not correo_valido:
                correo = input("Ingrese correo electrónico: ")
                correo_valido = self.validar_correo(correo)
                if not correo_valido:
                    print("La dirección de correo no es válida. Debe contener '@'.")
            
            nuevo_cliente = Cliente(nombre_cliente, contrasena, direccion, correo)
            self.base_de_datos[nombre_cliente] = nuevo_cliente
            print(f"Cliente '{nombre_cliente}' registrado exitosamente.")

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
