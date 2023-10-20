def año_bisiesto():
   
    try:
        año = int(input("Ingresa el año: "))
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


año_bisiesto()
