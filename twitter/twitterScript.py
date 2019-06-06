import twitter
import pymongo
import threading

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

def hacer_tweet():
    lista = []
    lista_enviar = []

    connection = pymongo.MongoClient('localhost', 27017)

    database = connection ['mydb_01']

    collectionCliente = database['consolidado']

    pipeline = [
        {"$group" : {"_id" : "$nombre", "count" : {"$sum" : "$total"}}},
        {"$sort" : {"count": -1}},
        {"$limit" : 3}
    ]

    cursos = collectionCliente.aggregate(pipeline)

    for x in cursos:
        lista.append(x)

    for i in lista:
        linea = str(i)

        separar = linea.split(', ')

        separar2 = separar[0].split(': ')

        enviar = separar2[1][1:len(separar2[1])-1]

        lista_enviar.append(enviar)

    primero = lista_enviar[0]
    segundo = lista_enviar[1]
    tercero = lista_enviar[2]


    post_update = api.PostUpdates(status = 'Prueba de proyecto: 1. {}, \n  2. {}, \n 3. {}'.format(primero, segundo, tercero))

    print(post_update)

def imprimirHola():
    print("Hello World")

def printit():
  threading.Timer(20.0, printit).start()
  hacer_tweet()
  print("tweet")

printit()

