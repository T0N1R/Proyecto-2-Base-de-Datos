# -*- coding: utf-8 -*-

import sys
import psycopg2
from psycopg2 import sql
from random import randint

productos = ["Leche", "Arroz", "Maizena", "cafe", "frijol", "sopa", "huevos", "Consomate", "harina de trigo", "azucar", 
             "aceite", "manteca", "papa", "jitomate", "chile rojo", "chile verde", "cebolla", "jabon", "cloro", "sal", 
             "naranjas", "platanos", "limones", "pinol", "pasta", "cervezas", "Quetzalteca", "Ron", "Tequila", "Burritos",
             "Yogurt descremado", "yogurt con frutas", "yogurt batido", "yogurt entero", "yogurt con cereales", "yogurt", "repelentes", "lavandinas",
             "lavavajillas", "limpiador de piso", "papel higiénico", "rollo de cocina", "jabón", "jabón en polvo", "jabón líquido", "suavizante para la ropa", "tapa de empanadas",
             "tapa de tartas", "crema enguaje", "champú", "desodorante femenino", "desodorante masculino", "alcohol", "crema dental", "tampones", "toallas higiénicas"]


conn = psycopg2.connect("dbname=proyecto2 user=postgres")

cur = conn.cursor()


def main(args):
    exitFlag = False

    while not exitFlag:
        print_menu()
        chosenOption = int(input("Ingrese su opción: "))

        if chosenOption == 0:
            cantidadProductos = input("Cuantos productos se acaban de ingresar al inventario? ")
            populateProduts(cantidadProductos)
        if chosenOption == 1:
            generateData(1)
        if chosenOption == 2:
            generateData(7)
        if chosenOption == 3:
            generateData(30)
        if chosenOption == 4:
            cantidadClientes = input("Cuantos clientes se acaban de ingresar al sistema? ")
            populateClients(cantidadClientes)
        if chosenOption == 5:
            exitFlag = True
        if chosenOption == 6:
            print("This is a hidden test option")
            currNit()


    conn.close()


def populateProduts(p_quantity):
    cur.execute('SELECT "id_producto" FROM productos ORDER BY "id_producto" DESC LIMIT 1')

    try:
        data = cur.fetchone()
        id_product = int(data[0])
    except Exception as exp:
        id_product=0

    for temp_product_id in range(int(id_product)+1, int(id_product)+1+int(p_quantity)):
        cur.execute(generateRandomProducts(temp_product_id))

    conn.commit()

    print("Se han ingresado los productos a la bodega")


def populateClients(c_quantity):
    cur.execute('SELECT "id_cliente" FROM clientes ORDER BY "id_cliente" DESC LIMIT 1')
    try:
        data=cur.fetchone()
        id_cliente=int(data[0])
    except Exception as exp:
        id_cliente=0
    for temp_id in range(int(id_cliente)+1,int(id_cliente)+1+int(c_quantity)):
        cur.execute(generateRandomClient(temp_id))
    conn.commit()


def lastClient():
    cur.execute('SELECT "id_cliente" FROM clientes ORDER BY "id_cliente" DESC LIMIT 1')
    try:
        data=cur.fetchone()
        id_cliente=int(data[0])
    except Exception as exp:
        id_cliente=0
    return id_cliente

def lastPrduct():
    cur.execute('SELECT "id_producto" FROM productos LIMIT 1')
    try:
        data=cur.fetchone()
        id_producto=int(data[0])
    except Exception as exp:
        id_producto=0
    return id_producto

def currClient():
    client = randint(1, int(lastClient()))
    cur.execute("SELECT nombre FROM clientes WHERE id_cliente = {}".format(client))
    try:
        data=cur.fetchone()
        client_name=str(data[0])
        print(client_name)
    except Exception as exp:
        client_name=""
    return client_name

def currNit():
    client = randint(1, int(lastClient()))
    cur.execute("SELECT nit FROM clientes WHERE id_cliente = {}".format(client))
    try:
        data=cur.fetchone()
        client_nit=str(data[0])
        print(client_nit)
    except Exception as exp:
        client_nit=""
    return client_nit


def generateData(days):
    cur.execute('SELECT "id_factura" FROM factura ORDER BY "id_factura" DESC LIMIT 1')

    try:
        data = cur.fetchone()
        id_factura = int(data[0])
    except Exception as exp:
        id_factura=0

    cur.execute('SELECT "id_linea_factura" FROM linea_factura ORDER BY "id_linea_factura" DESC LIMIT 1')

    try:
        data = cur.fetchone()
        id_linea = data[0]
    except Exception as exp:
        id_linea=0

    for temp_id_factura in range(id_factura+1, id_factura +1+ days * randint(1, 10000)):
        cur.execute(generateRandomReceipt(temp_id_factura))
        print("Se han generado las facturas vacias")
        count_line = randint(1, 10)
        for temp_linea in range(id_linea+1, id_linea + count_line):
            cur.execute(generateRandomLine(temp_linea, temp_id_factura))
            print("Se ha llenado la factura")
        id_linea = id_linea + count_line

    conn.commit()

    print("Se han generado los registros de los dias indicados")


def getClientID():
    return randint(1, 59)


def getRandomArrayFromOpts(opts):
    return opts[randint(0, len(opts)-1)]


def getRandomDate():
    return str(randint(2015, 2020)) + "/" + str(randint(1, 12)) + "/" + str(randint(1, 28))


def generateRandomReceipt(id_factura):
    return('INSERT INTO "factura" ("id_factura", "nombre", "nit", "descripcion", "fecha", "total") VALUES (' + str(id_factura) + ', ' + "'" + "cliente" + str(randint(1, int(lastClient()))) + "'" + ', ' + str(randint(1000000, 99999999)) + ', ' + "'" + str("a") + "'" + ', ' +"'"+ str(getRandomDate()) +"'"+ ', ' + str(randint(0, 9999)) +');')


def generateRandomLine(cant, factura):
    return('INSERT INTO "linea_factura" ("id_linea_factura", "id_factura", "id_producto", "cantidad", "precio") VALUES ('+ str(cant) + ', '+ str(factura) + ', ' + str(randint(1, int(lastPrduct()))) + ',' + str(randint(1, 3)) + ', '+str(randint(1,99))+ ');')

def generateRandomProducts(id_product):
    return('INSERT INTO "productos" ("id_producto", "nombre", "precio") VALUES (' + str(id_product) + ', ' +"'" + str(getRandomArrayFromOpts(productos)) +"'" + ', ' + str(randint(0, 999)) + ');')


def generateRandomClient(temp_id):
     return('INSERT INTO "clientes" ("id_cliente", "nombre", "nit") VALUES (' + str(temp_id) + ', ' +"'" + "cliente"+str(temp_id) +"'" + ', ' + str(randint(1000000, 99999999)) + ');')


def print_menu():
    print("")
    print(" 0) Ingresar data de ingreso para la bodega")
    print(" 1) Generar data para un dia")
    print(" 2) Generar data para una semana")
    print(" 3) Generar data para un mes")
    print(" 4) Ingresar clientes del dia")
    print(" 5) Salir")


if __name__ == '__main__':
    main(sys.argv)
