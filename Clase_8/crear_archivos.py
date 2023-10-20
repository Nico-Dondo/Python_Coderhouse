# Open es para crear un archivo
mi_archivo = open("mi_primer_archivo.txt", "w") 

# Write es para escribir en el archivo creado
mi_archivo.write("Esta es la primer linea que escribo!")
mi_archivo.write("Esta es la segunda linea que escribo!")

# Writelines es para escribir en lineas y para que la separe es necesario utilizar \n
mi_archivo.writelines(
    [
        "Esta es la primer linea que escribo!\n",
        "Esta es la segunda linea que escribo!\n",
        "=)"
    ]
)