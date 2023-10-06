
año_nacimiento = int(input("Ingresa el año de nacimiento: "))


if 1920 <= año_nacimiento <= 1945:
    generacion = "Generacion Silenciosa"
elif 1946 <= año_nacimiento <= 1964:
    generacion = "Baby Boomer"
elif 1965 <= año_nacimiento <= 1980:
    generacion = "Generación X"
elif 1981 <= año_nacimiento <= 1996:
    generacion = "Millennial"
elif 1997 <= año_nacimiento <= 2012:
    generacion = "Generación Z"
else:
    generacion = "Generación Desconocida"


print(f"La persona que nació en {año_nacimiento} pertenece a la generación: {generacion}")
