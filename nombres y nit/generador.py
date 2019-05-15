from random import randint


nombres = []
apellidos = []

f = open("nombres.txt", "r")
for x in f:
    separado = x.split()
    nombres.append(separado[0])
    apellidos.append(separado[1])



contador = 100

while contador > 0:
    randNIT = randint(1000000, 10000000) 
    varchar = str(randNIT)
    nit_guion = varchar[0:len(varchar) -1 ] + "-" + varchar[len(varchar) - 1: len(varchar)]

    print(nombres[randint(0, len(nombres) - 1 )], apellidos[randint(0, len(nombres) - 1 )], nit_guion)
    contador -= 1
    
