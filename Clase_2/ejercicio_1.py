""" my_string ="abracadabra",

print(my_string) # para mprimir por terminal lo que se declaro en la variable

print(len("abracadabra"))# para ver la cantidad de letras que contiene en este caso abracadabra
print("******************************************")
mi_numero = 9  #otra funcion con numero

print(mi_numero)
print("******************************************")

#LISTAS
mi_lista =[1, 2, "A"] # es un array

print(mi_lista[0]) # entre corchetes se pasa la ubicacion 
print("******************************************")

otra_lista = ("a","b","c","d","e","f")
print(otra_lista[0:3]) # para imprimir por ubicacion
print(otra_lista[-1]) # imprime desde el ultimo valor de la lista o array

print (f"El primer elemento de mi lista es {otra_lista[0]}") # el f es para pasar cadena y entre llaves va lo que se quiere imprimir y el valor o ubicacion entre []

print("******************************************")# a modo de ejemplo para separar """

otra_lista = ["a","b","c","d","e","f","a"] # para usar el append tiene que estar entrer corchetes
print("******************************************")
print(otra_lista)
""" print("******************************************")
print(len(otra_lista))
print("******************************************")
otra_lista.append("Elemento que quiero agregar") #append parra agregar cadena a lo que se quiere imprimir
print(otra_lista)
print("******************************************")

print(otra_lista.count("a")) """# el count es ara contar la cantidad de parametros que le pasamos

print(otra_lista.index("b")) # se usa el index para saber en que lugar esta