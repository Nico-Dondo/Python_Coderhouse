from time import sleep, time
import random
import sqlite3


mi_archivo = open("mi_segundo_archivo.txt", "w")

for i in range(10):
    xx = str(random.randint(0, 19))
    mi_archivo.write(xx)
    mi_archivo.write(",")