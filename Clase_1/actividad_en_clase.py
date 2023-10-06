# Pedir cantidad de partidos, ganados, empatados y perdidos
partidos_ganados = int(input("Ingresa la cantidad de partidos ganados"))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

# Puntos asignados por partido 
puntos_partido_ganado = 3
puntos_partido_empatado = 1
puntos_partido_perdido = 0
partidos_jugados = 20

# Operacion
puntos_obtenidos = (partidos_ganados * puntos_partido_ganado
                  + partidos_empatados * puntos_partido_empatado
                  + partidos_perdidos * puntos_partido_perdido)
promedio = puntos_obtenidos / partidos_jugados


print("EL promedio final de puntos es", {promedio})