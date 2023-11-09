
from clientes import ManejadorClientes, Cliente
from productos import ManejadorProductos, Producto

def main():
    manejador_clientes = ManejadorClientes()
    manejador_productos = ManejadorProductos()

    while True:
        print("\n1. Registrar nuevo cliente")
        print("2. Mostrar clientes registrados")
        print("3. Registrar nuevo producto")
        print("4. Mostrar productos registrados")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            manejador_clientes.registrar_cliente()
        elif opcion == '2':
            manejador_clientes.mostrar_clientes()
        elif opcion == '3':
            manejador_productos.registrar_producto()
        elif opcion == '4':
            manejador_productos.mostrar_productos()
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            manejador_clientes.guardar_base_datos()
            manejador_productos.guardar_base_datos()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
