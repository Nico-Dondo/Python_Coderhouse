# edad = input ("Ingrese su edad:")

# edad =int(edad)

edad = input ("Ingrese su edad:")

antiguedad = input ("ingrese su antiguedad:")

ingreso = input ("ingresar su ingreso:")

if not (edad.isnumeric() and antiguedad.isnumeric() and ingreso.isnumeric()):
    print(f"Por favor ingrese un valor numerico. Usted ha ingresado: {edad} {antiguedad} {ingreso}")
else:
    edad =int (edad )
    antiguedad = int (antiguedad)
    ingreso = int (ingreso)
    if edad < 18:
        print("Crédito denegado")
    else:
        if antiguedad >= 3 and ingreso >= 2500:
            print("Credito Aprobado")
        elif antiguedad < 3 and ingreso >= 4000:
            print("Credito aprobado")
     
