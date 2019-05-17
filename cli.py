# -*- coding: utf-8 -*-

import sys
import psycopg2
from random import randint

productos = ["Leche", "Arroz", "Maizena", "cafe", "frijol", "sopa", "huevos", "Consomate", "harina de trigo", "azucar", 
             "aceite", "manteca", "papa", "jitomate", "chile rojo", "chile verde", "cebolla", "jabon", "cloro", "sal", 
             "naranjas", "platanos", "limones", "pinol", "pasta", "cervezas", "Quetzalteca", "Ron", "Tequila", "Burritos"]

conn = psycopg2.connect("dbname=proyecto2 user=postgres")

cur = conn.cursor()
temp_inline_holder = 0


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
            exitFlag = true

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

def generateData(days):
    cur.execute('SELECT "id_factura" FROM factura ORDER BY "id_factura" DESC LIMIT 1')

    try:
        data = cur.fetchone()
        id_factura = int(data[0])
    except Exception as exp:
        id_factura=0

    cur.execute('SELECT "id_linea_factura" FROM linea_factura ORDER BY "invoicelineId" DESC LIMIT 1')

    try:
        data = cur.fetchone()
        id_linea = data[0]
    except Exception as exp:
        id_linea=0

    for temp_id_factura in range(id_factura+1, id_factura +1+ days * randint(1, 10)):
        cur.execute(generateRandomReceipt(temp_id_factura)
        print("Se han generado las facturas vacias")
        count_line = randint(1, 10)
        for temp_linea in range(id_linea+1, id_linea + count_line:
            cur.execute(generateRandomLine(temp_linea, temp_id_factura))
            print("Se ha llenado la factura")
        id_linea = id_linea + count_line

    print("Se han generado los registros de los dias indicados")


def getClientID():
    return randint(1, 59)


def getRandomArrayFromOpts(opts):
    return opts[randint(0, len(opts)-1)]


def getRandomDate():
    return str(randint(2015, 2020)) + "/" + str(randint(1, 12)) + "/" + str(randint(1, 28))


def getRandomTrackID():
    return randint(1, 3503)


def generateRandomInvoice(invoiceId, customerID):
    print('INSERT INTO "invoice" ("invoiceId", "customerId", "invoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry", "BillingPostalCode", "Total") VALUES (' + str(invoiceId) + ', ' + str(customerID) + ', \'' + str(getRandomDate()) + '\', \'' + str(getRandomArrayFromOpts(adresses)) + '\', \'' + str(getRandomArrayFromOpts(towns)) + '\', \'' + str(getRandomArrayFromOpts(cities)) + '\', \'USA\', \'' + str(randint(1010, 9999)) + '\', 0.99);')
    return str('INSERT INTO "invoice" ("invoiceId", "customerId", "invoiceDate", "BillingAddress", "BillingCity", "BillingState", "BillingCountry", "BillingPostalCode", "Total") VALUES (' + str(invoiceId) + ', ' + str(customerID) + ', \'' + str(getRandomDate()) + '\', \'' + str(getRandomArrayFromOpts(adresses)) + '\', \'' + str(getRandomArrayFromOpts(towns)) + '\', \'' + str(getRandomArrayFromOpts(cities)) + '\', \'USA\', \'' + str(randint(1010, 9999)) + '\', 0.99);')

def generateRandomInvoiceLine(invoiceLineId, invoiceId):
    print('INSERT INTO "invoiceline" ("invoicelineId", "invoiceId", "trackId", "UnitPrice", "Quantity") VALUES (' + str(invoiceLineId) + ', ' + str(invoiceId) + ', ' + str(getRandomTrackID()) + ', 0.99, 1);')
    return str('INSERT INTO "invoiceline" ("invoicelineId", "invoiceId", "trackId", "UnitPrice", "Quantity") VALUES (' + str(invoiceLineId) + ', ' + str(invoiceId) + ', ' + str(getRandomTrackID()) + ', 0.99, 1);')

def generateRandomProducts(id_product):
    return('INSERT INTO "productos" ("id_producto", "nombre", "precio") VALUES (' + str(id_product) + ', ' +"'" + str(getRandomArrayFromOpts(productos)) +"'" + ', ' + str(randint(0, 999)) + ');')

def print_menu():
    print("")
    print(" 0) Ingresar data de ingreso para la bodega")
    print(" 2) Generar data para un dia")
    print(" 2) Generar data para una semana")
    print(" 3) Generar data para un mes")
    print(" 4) Salir")


if __name__ == '__main__':
    main(sys.argv)
