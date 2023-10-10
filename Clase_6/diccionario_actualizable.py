from pprint import pprint


dict_1 = {}
for i in range(100):
    dict_1[i] = "1"

# print("dict_1 ->", dict_1)
pprint(dict_1)

# Modificar el loop anterior para que en vez de que todos los valores sean "i"
# tener que cada valor es igual a su clave correspondiente
dict_2 = {}
for i in range(20):
    dict_2[+i] = i

# print("dict_1 ->", dict_1)
pprint(dict_2)