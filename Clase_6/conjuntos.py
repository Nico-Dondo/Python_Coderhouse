conjunto_0 = set()
conjunto_1 = { 1,2,3,4}

print(conjunto_0)
print(conjunto_1)
print ("-" * 90)

# Para hacer intersecciones entre conjuntos, que son los elementos en comun
interseccion = conjunto_1.intersection(conjunto_0)
print(interseccion)

# Agregado un elemento y debajo pasamo el mismo comando para buscar los elementos en comun
conjunto_0.add(1)
interseccion = conjunto_1.intersection(conjunto_0)
print(conjunto_0)
print(conjunto_1)
print(interseccion)
print ("-" * 90)

# Union de conjuntos
conjunto_0.add(1,)
print(conjunto_0)
print(conjunto_1)
union = conjunto_1.intersection(conjunto_0)
print(union)
print ("-" * 90)



