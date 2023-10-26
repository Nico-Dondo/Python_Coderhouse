def año_bisiesto():
    año = input("Ingresa el año: ")

    if año.isdigit(): 
        año = int(año) 
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")
    else:
        print("Por favor, ingresa un número válido.")

año_bisiesto()