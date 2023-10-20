import sqlite3

# Conectar a la base de datos (si no existe, se creará)
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear un objeto cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla de ejemplo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
''')

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
