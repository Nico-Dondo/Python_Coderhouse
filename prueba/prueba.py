# Registro de usuarios
def registro():
    mis_users = {}

    while True:
        usuario = input("Ingrese nombre de usuario (o escriba 'inicio' para iniciar sesión): ")
        if usuario.lower() == 'inicio':
            if mis_users:
                inicio_de_sesion(mis_users)
                break
            else:
                print("No hay usuarios registrados. Registre al menos uno primero.")
        else:
            password = input("Ingrese su contraseña: ")
            mis_users[usuario] = password
            print(f"Usuario: {usuario} creado con éxito")

    return mis_users


def mostrar_info(usuarios):
    if usuarios:
        for usuario, password in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {password}")
    else:
        print("No hay usuarios registrados.")


def inicio_de_sesion(usuarios):
    if not usuarios:
        print("No hay usuarios registrados. Registre al menos uno primero.")
        return

    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if usuario in usuarios:
        if usuarios[usuario] == password:
            print(f"Bienvenido {usuario}, inicio de sesión exitoso")
        else:
            print("Contraseña incorrecta, por favor intente de nuevo.")
    else:
        print("Usuario no encontrado, por favor regístrese.")


usuarios = registro()


mostrar_info(usuarios)
