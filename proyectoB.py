# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Antonio\Documents\Stuff\Base de Datos\proyectoBD\proyecto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import psycopg2

productosTabla = []
enviarTotal = 0.00
claveBD = "060f3d4eae"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tota_precio = QtWidgets.QTabWidget(self.centralwidget)
        self.tota_precio.setGeometry(QtCore.QRect(0, 0, 971, 531))
        self.tota_precio.setObjectName("tota_precio")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tabClientes)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 971, 501))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.clientesConsultar = QtWidgets.QWidget()
        self.clientesConsultar.setObjectName("clientesConsultar")
        self.tabla_cliente = QtWidgets.QTableWidget(self.clientesConsultar)
        self.tabla_cliente.setGeometry(QtCore.QRect(280, 10, 471, 341))
        self.tabla_cliente.setRowCount(0)
        self.tabla_cliente.setColumnCount(3)
        self.tabla_cliente.setObjectName("tabla_cliente")
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_cliente.setHorizontalHeaderItem(2, item)
        self.consulta_id_cliente = QtWidgets.QTextEdit(self.clientesConsultar)
        self.consulta_id_cliente.setGeometry(QtCore.QRect(110, 30, 141, 41))
        self.consulta_id_cliente.setObjectName("consulta_id_cliente")
        self.buscar_cliente = QtWidgets.QPushButton(self.clientesConsultar)
        self.buscar_cliente.setGeometry(QtCore.QRect(70, 220, 91, 41))
        self.buscar_cliente.setObjectName("buscar_cliente")
        self.label_7 = QtWidgets.QLabel(self.clientesConsultar)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 51, 21))
        self.label_7.setObjectName("label_7")
        self.consulta_nombre_cliente = QtWidgets.QTextEdit(self.clientesConsultar)
        self.consulta_nombre_cliente.setGeometry(QtCore.QRect(110, 90, 141, 41))
        self.consulta_nombre_cliente.setObjectName("consulta_nombre_cliente")
        self.label_8 = QtWidgets.QLabel(self.clientesConsultar)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 61, 21))
        self.label_8.setObjectName("label_8")
        self.consulta_nit_cliente = QtWidgets.QTextEdit(self.clientesConsultar)
        self.consulta_nit_cliente.setGeometry(QtCore.QRect(110, 150, 141, 41))
        self.consulta_nit_cliente.setObjectName("consulta_nit_cliente")
        self.label_9 = QtWidgets.QLabel(self.clientesConsultar)
        self.label_9.setGeometry(QtCore.QRect(40, 160, 41, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.clientesConsultar)
        self.label_10.setGeometry(QtCore.QRect(20, 5, 271, 21))
        self.label_10.setObjectName("label_10")
        self.tabWidget_2.addTab(self.clientesConsultar, "")
        self.clientesInsertar = QtWidgets.QWidget()
        self.clientesInsertar.setObjectName("clientesInsertar")
        self.label = QtWidgets.QLabel(self.clientesInsertar)
        self.label.setGeometry(QtCore.QRect(20, 20, 35, 16))
        self.label.setObjectName("label")
        self.id_cliente = QtWidgets.QTextEdit(self.clientesInsertar)
        self.id_cliente.setGeometry(QtCore.QRect(90, 10, 141, 31))
        self.id_cliente.setObjectName("id_cliente")
        self.label_2 = QtWidgets.QLabel(self.clientesInsertar)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.nombre_cliente = QtWidgets.QTextEdit(self.clientesInsertar)
        self.nombre_cliente.setGeometry(QtCore.QRect(90, 50, 141, 31))
        self.nombre_cliente.setObjectName("nombre_cliente")
        self.label_3 = QtWidgets.QLabel(self.clientesInsertar)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 35, 16))
        self.label_3.setObjectName("label_3")
        self.nit_cliente = QtWidgets.QTextEdit(self.clientesInsertar)
        self.nit_cliente.setGeometry(QtCore.QRect(90, 90, 141, 31))
        self.nit_cliente.setObjectName("nit_cliente")
        self.insert_cliente = QtWidgets.QPushButton(self.clientesInsertar)
        self.insert_cliente.setGeometry(QtCore.QRect(90, 150, 71, 41))
        self.insert_cliente.setObjectName("insert_cliente")
        self.tabWidget_2.addTab(self.clientesInsertar, "")
        self.tota_precio.addTab(self.tabClientes, "")
        self.tabProductos = QtWidgets.QWidget()
        self.tabProductos.setObjectName("tabProductos")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tabProductos)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 971, 491))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.productosConsultar = QtWidgets.QWidget()
        self.productosConsultar.setObjectName("productosConsultar")
        self.label_11 = QtWidgets.QLabel(self.productosConsultar)
        self.label_11.setGeometry(QtCore.QRect(20, 5, 271, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.productosConsultar)
        self.label_12.setGeometry(QtCore.QRect(30, 100, 61, 21))
        self.label_12.setObjectName("label_12")
        self.consulta_id_producto = QtWidgets.QTextEdit(self.productosConsultar)
        self.consulta_id_producto.setGeometry(QtCore.QRect(110, 30, 141, 41))
        self.consulta_id_producto.setObjectName("consulta_id_producto")
        self.consulta_precio_producto = QtWidgets.QTextEdit(self.productosConsultar)
        self.consulta_precio_producto.setGeometry(QtCore.QRect(110, 150, 141, 41))
        self.consulta_precio_producto.setObjectName("consulta_precio_producto")
        self.label_13 = QtWidgets.QLabel(self.productosConsultar)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 51, 21))
        self.label_13.setObjectName("label_13")
        self.consulta_nombre_producto = QtWidgets.QTextEdit(self.productosConsultar)
        self.consulta_nombre_producto.setGeometry(QtCore.QRect(110, 90, 141, 41))
        self.consulta_nombre_producto.setObjectName("consulta_nombre_producto")
        self.label_14 = QtWidgets.QLabel(self.productosConsultar)
        self.label_14.setGeometry(QtCore.QRect(40, 40, 51, 21))
        self.label_14.setObjectName("label_14")
        self.buscar_producto = QtWidgets.QPushButton(self.productosConsultar)
        self.buscar_producto.setGeometry(QtCore.QRect(70, 220, 91, 41))
        self.buscar_producto.setObjectName("buscar_producto")
        self.tabla_producto = QtWidgets.QTableWidget(self.productosConsultar)
        self.tabla_producto.setGeometry(QtCore.QRect(280, 10, 471, 341))
        self.tabla_producto.setRowCount(0)
        self.tabla_producto.setColumnCount(3)
        self.tabla_producto.setObjectName("tabla_producto")
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(2, item)
        self.tabWidget_3.addTab(self.productosConsultar, "")
        self.productosInsertar = QtWidgets.QWidget()
        self.productosInsertar.setObjectName("productosInsertar")
        self.label_4 = QtWidgets.QLabel(self.productosInsertar)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 35, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.productosInsertar)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_5.setObjectName("label_5")
        self.nombre_producto = QtWidgets.QTextEdit(self.productosInsertar)
        self.nombre_producto.setGeometry(QtCore.QRect(90, 50, 141, 31))
        self.nombre_producto.setObjectName("nombre_producto")
        self.label_6 = QtWidgets.QLabel(self.productosInsertar)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.label_6.setObjectName("label_6")
        self.precio_producto = QtWidgets.QTextEdit(self.productosInsertar)
        self.precio_producto.setGeometry(QtCore.QRect(90, 90, 141, 31))
        self.precio_producto.setObjectName("precio_producto")
        self.id_producto = QtWidgets.QTextEdit(self.productosInsertar)
        self.id_producto.setGeometry(QtCore.QRect(90, 10, 141, 31))
        self.id_producto.setObjectName("id_producto")
        self.insert_producto = QtWidgets.QPushButton(self.productosInsertar)
        self.insert_producto.setGeometry(QtCore.QRect(90, 150, 71, 41))
        self.insert_producto.setObjectName("insert_producto")
        self.tabWidget_3.addTab(self.productosInsertar, "")
        self.tota_precio.addTab(self.tabProductos, "")
        self.tabVentas = QtWidgets.QWidget()
        self.tabVentas.setObjectName("tabVentas")
        self.total_ventas = QtWidgets.QLabel(self.tabVentas)
        self.total_ventas.setGeometry(QtCore.QRect(550, 410, 180, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.total_ventas.setFont(font)
        self.total_ventas.setObjectName("total_ventas")
        self.tabla_ventas = QtWidgets.QTableWidget(self.tabVentas)
        self.tabla_ventas.setGeometry(QtCore.QRect(420, 60, 471, 341))
        self.tabla_ventas.setRowCount(0)
        self.tabla_ventas.setColumnCount(3)
        self.tabla_ventas.setObjectName("tabla_ventas")
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas.setHorizontalHeaderItem(2, item)
        self.pago = QtWidgets.QPushButton(self.tabVentas)
        self.pago.setGeometry(QtCore.QRect(760, 420, 91, 41))
        self.pago.setObjectName("pago")
        self.label_16 = QtWidgets.QLabel(self.tabVentas)
        self.label_16.setGeometry(QtCore.QRect(10, 90, 61, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tabVentas)
        self.label_17.setGeometry(QtCore.QRect(10, 140, 101, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tabVentas)
        self.label_18.setGeometry(QtCore.QRect(20, 190, 41, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tabVentas)
        self.label_19.setGeometry(QtCore.QRect(10, 240, 51, 21))
        self.label_19.setObjectName("label_19")
        self.nombre_para_factura = QtWidgets.QTextEdit(self.tabVentas)
        self.nombre_para_factura.setGeometry(QtCore.QRect(100, 80, 161, 41))
        self.nombre_para_factura.setObjectName("nombre_para_factura")
        self.direccion_factura = QtWidgets.QTextEdit(self.tabVentas)
        self.direccion_factura.setGeometry(QtCore.QRect(100, 130, 161, 41))
        self.direccion_factura.setObjectName("direccion_factura")
        self.nit_factura = QtWidgets.QTextEdit(self.tabVentas)
        self.nit_factura.setGeometry(QtCore.QRect(100, 180, 161, 41))
        self.nit_factura.setObjectName("nit_factura")
        self.fecha = QtWidgets.QTextEdit(self.tabVentas)
        self.fecha.setGeometry(QtCore.QRect(100, 230, 161, 41))
        self.fecha.setObjectName("fecha")
        self.label_20 = QtWidgets.QLabel(self.tabVentas)
        self.label_20.setGeometry(QtCore.QRect(90, 0, 271, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tabVentas)
        self.label_21.setGeometry(QtCore.QRect(100, 280, 161, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tabVentas)
        self.label_22.setGeometry(QtCore.QRect(4, 310, 91, 20))
        self.label_22.setObjectName("label_22")
        self.producto_para_factura = QtWidgets.QTextEdit(self.tabVentas)
        self.producto_para_factura.setGeometry(QtCore.QRect(100, 300, 161, 41))
        self.producto_para_factura.setObjectName("producto_para_factura")
        self.label_23 = QtWidgets.QLabel(self.tabVentas)
        self.label_23.setGeometry(QtCore.QRect(10, 360, 61, 16))
        self.label_23.setObjectName("label_23")
        self.cantidad_producto = QtWidgets.QTextEdit(self.tabVentas)
        self.cantidad_producto.setGeometry(QtCore.QRect(100, 350, 161, 41))
        self.cantidad_producto.setObjectName("cantidad_producto")
        self.borrar_ventas = QtWidgets.QPushButton(self.tabVentas)
        self.borrar_ventas.setGeometry(QtCore.QRect(800, 10, 91, 41))
        self.borrar_ventas.setObjectName("borrar_ventas")
        self.pushButton_3 = QtWidgets.QPushButton(self.tabVentas)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 410, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.id_factura = QtWidgets.QTextEdit(self.tabVentas)
        self.id_factura.setGeometry(QtCore.QRect(100, 30, 161, 41))
        self.id_factura.setObjectName("id_factura")
        self.label_24 = QtWidgets.QLabel(self.tabVentas)
        self.label_24.setGeometry(QtCore.QRect(10, 40, 91, 20))
        self.label_24.setObjectName("label_24")
        self.tota_precio.addTab(self.tabVentas, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConsulta = QtWidgets.QAction(MainWindow)
        self.actionConsulta.setObjectName("actionConsulta")
        self.actionInsertar = QtWidgets.QAction(MainWindow)
        self.actionInsertar.setObjectName("actionInsertar")
        self.actionConsulta_2 = QtWidgets.QAction(MainWindow)
        self.actionConsulta_2.setObjectName("actionConsulta_2")
        self.actionInsertar_2 = QtWidgets.QAction(MainWindow)
        self.actionInsertar_2.setObjectName("actionInsertar_2")
        self.actionConsulta_3 = QtWidgets.QAction(MainWindow)
        self.actionConsulta_3.setObjectName("actionConsulta_3")
        self.actionInsertar_3 = QtWidgets.QAction(MainWindow)
        self.actionInsertar_3.setObjectName("actionInsertar_3")

        self.retranslateUi(MainWindow)
        self.tota_precio.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ########### BOTONES ###########
        ###############################

        self.buscar_cliente.clicked.connect(self.buscarCliente)
        self.buscar_producto.clicked.connect(self.buscarProducto)
        self.insert_cliente.clicked.connect(self.insertCliente)
        self.insert_producto.clicked.connect(self.insertProducto)
        self.pushButton_3.clicked.connect(self.ventas)
        self.borrar_ventas.clicked.connect(self.borrarVentas)
        self.pago.clicked.connect(self.finalizarVentas)

        ###############################
        ########### BOTONES ###########


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tabla_cliente.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tabla_cliente.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_cliente.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NIT"))
        self.buscar_cliente.setText(_translate("MainWindow", "Buscar"))
        self.label_7.setText(_translate("MainWindow", "ID: "))
        self.label_8.setText(_translate("MainWindow", "Nombre: "))
        self.label_9.setText(_translate("MainWindow", "NIT:"))
        self.label_10.setText(_translate("MainWindow", "Ingresa los datos"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.clientesConsultar), _translate("MainWindow", "Consultar"))
        self.label.setText(_translate("MainWindow", "ID: "))
        self.label_2.setText(_translate("MainWindow", "Nombre: "))
        self.label_3.setText(_translate("MainWindow", "NIT: "))
        self.insert_cliente.setText(_translate("MainWindow", "Insertar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.clientesInsertar), _translate("MainWindow", "Insertar"))
        self.tota_precio.setTabText(self.tota_precio.indexOf(self.tabClientes), _translate("MainWindow", "Clientes"))
        self.label_11.setText(_translate("MainWindow", "Ingresa los datos"))
        self.label_12.setText(_translate("MainWindow", "Nombre: "))
        self.label_13.setText(_translate("MainWindow", "Precio: "))
        self.label_14.setText(_translate("MainWindow", "ID: "))
        self.buscar_producto.setText(_translate("MainWindow", "Buscar"))
        item = self.tabla_producto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tabla_producto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_producto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.productosConsultar), _translate("MainWindow", "Consultar"))
        self.label_4.setText(_translate("MainWindow", "ID: "))
        self.label_5.setText(_translate("MainWindow", "Nombre: "))
        self.label_6.setText(_translate("MainWindow", "Precio: "))
        self.insert_producto.setText(_translate("MainWindow", "Insertar"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.productosInsertar), _translate("MainWindow", "Insertar"))
        self.tota_precio.setTabText(self.tota_precio.indexOf(self.tabProductos), _translate("MainWindow", "Productos"))
        self.total_ventas.setText(_translate("MainWindow", "Q0.00"))
        item = self.tabla_ventas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tabla_ventas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_ventas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio"))
        self.pago.setText(_translate("MainWindow", "Pago"))
        self.label_16.setText(_translate("MainWindow", "Nombre: "))
        self.label_17.setText(_translate("MainWindow", "Dirección: "))
        self.label_18.setText(_translate("MainWindow", "NIT: "))
        self.label_19.setText(_translate("MainWindow", "Fecha: "))
        self.label_20.setText(_translate("MainWindow", "Datos de factura"))
        self.label_21.setText(_translate("MainWindow", "Productos de venta"))
        self.label_22.setText(_translate("MainWindow", "id Producto: "))
        self.label_23.setText(_translate("MainWindow", "Cantidad: "))
        self.borrar_ventas.setText(_translate("MainWindow", "Borrar"))
        self.pushButton_3.setText(_translate("MainWindow", "Agregar"))
        self.label_24.setText(_translate("MainWindow", "id Factura:"))
        self.tota_precio.setTabText(self.tota_precio.indexOf(self.tabVentas), _translate("MainWindow", "Ventas"))
        self.actionConsulta.setText(_translate("MainWindow", "Consulta"))
        self.actionInsertar.setText(_translate("MainWindow", "Insertar"))
        self.actionConsulta_2.setText(_translate("MainWindow", "Consulta"))
        self.actionInsertar_2.setText(_translate("MainWindow", "Insertar"))
        self.actionConsulta_3.setText(_translate("MainWindow", "Consulta"))
        self.actionInsertar_3.setText(_translate("MainWindow", "Insertar"))

    global claveBD

    def buscarCliente(self):
        #id del cliente
        a = self.consulta_id_cliente.toPlainText()

        #nombre del cliente
        b = self.consulta_nombre_cliente.toPlainText()

        #nit del cliente
        c = self.consulta_nit_cliente.toPlainText()

        self.consulta_id_cliente.clear()
        self.consulta_nombre_cliente.clear()
        self.consulta_nit_cliente.clear()

        #solo se escribe el id
        if a != "" and b == "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE id_cliente = '{}';".format(a))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()
        
        #solo se escribe el nombre
        if a == "" and b != "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE nombre = '{}';".format(b))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #solo se escribe el nit
        if a == "" and b == "" and c != "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE nit = '{}';".format(c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #id y nombre
        if a != "" and b != "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE id_cliente = '{}' AND nombre = '{}';".format(a, b))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #id y nit
        if a != "" and b == "" and c != "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE id_cliente = '{}' AND nit = '{}';".format(a, c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #nombre y nit
        if a == "" and b != "" and c != "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE nombre = '{}' AND nit = '{}';".format(b, c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #todos
        if a != "" and b != "" and c!= "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes WHERE id_cliente = '{}' AND nombre = '{}' AND nit = '{}';".format(a,b,c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #ninguno
        if a == "" and b == "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Clientes;")
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_cliente.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_cliente.setRowCount(row + 1)

                self.tabla_cliente.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_cliente.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_cliente.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

    def buscarProducto(self):
        #id del cliente
        a = self.consulta_id_producto.toPlainText()

        #nombre del cliente
        b = self.consulta_nombre_producto.toPlainText()

        #nit del cliente
        c = self.consulta_precio_producto.toPlainText()

        self.consulta_id_producto.clear()
        self.consulta_nombre_producto.clear()
        self.consulta_precio_producto.clear()

        #solo se escribe el id
        if a != "" and b == "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE id_producto = '{}';".format(a))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()
        
        #solo se escribe el nombre
        if a == "" and b != "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE nombre = '{}';".format(b))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #solo se escribe el precio
        if a == "" and b == "" and c != "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE precio = '{}';".format(c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #id y nombre
        if a != "" and b != "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE id_producto = '{}' AND nombre = '{}';".format(a, b))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #id y precio
        if a != "" and b == "" and c != "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE id_producto = '{}' AND precio = '{}';".format(a, c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #nombre y nit
        if a == "" and b != "" and c != "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE nombre = '{}' AND precio = '{}';".format(b, c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #todos
        if a != "" and b != "" and c!= "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos WHERE id_producto = '{}' AND nombre = '{}' AND precio = '{}';".format(a,b,c))
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

        #ninguno
        if a == "" and b == "" and c == "":
            
            conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

            #cursor para hacer operaciones en la database
            cur = conn.cursor()
            
            result = cur.execute("SELECT * FROM Productos;")
            conn.commit()

            rows = cur.fetchall()

            enviar = []

            for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                enviar.append(fila)

            self.tabla_producto.clearContents()

            row = 0

            for edian in enviar:
                self.tabla_producto.setRowCount(row + 1)

                self.tabla_producto.setItem(row, 0, QTableWidgetItem(edian[0]))
                self.tabla_producto.setItem(row, 1, QTableWidgetItem(edian[1]))
                self.tabla_producto.setItem(row, 2, QTableWidgetItem(edian[2]))

                row += 1


            conn.close()

    def insertCliente(self):

        
        conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

        #cursor para hacer operaciones en la database
        cur = conn.cursor()

        #id del cliente
        a = self.id_cliente.toPlainText()

        #nombre del cliente
        b = self.nombre_cliente.toPlainText()

        #nit del cliente
        c = self.nit_cliente.toPlainText()

        self.id_cliente.clear()
        self.nombre_cliente.clear()
        self.nit_cliente.clear()

        cur.execute("INSERT INTO Clientes (id_cliente, nombre, NIT) VALUES(\
                    '{}', \
                    '{}',\
                     '{}');".format(str(a), str(b), str(c)))

        conn.commit()
        conn.close()

        print("nuevo cliente")
            
    def insertProducto(self):

        
        conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

        #cursor para hacer operaciones en la database
        cur = conn.cursor()

        #id del producto
        a = self.id_producto.toPlainText()

        #nombre del producto
        b = self.nombre_producto.toPlainText()

        #precio del producto
        c = self.precio_producto.toPlainText()

        self.id_producto.clear()
        self.nombre_producto.clear()
        self.precio_producto.clear()

        cur.execute("INSERT INTO Productos (id_producto, nombre, precio) VALUES( \
                    '{}', \
                	'{}', \
	                 {});".format(str(a), str(b), float(c)))

        conn.commit()
        conn.close()

        print("nuevo producto")
        
    def ventas(self):
        #id factura
        a = int(self.id_factura.toPlainText())

        #nombre para factura 
        b = self.nombre_para_factura.toPlainText()

        #direccion factura
        c = self.direccion_factura.toPlainText()

        #nit para factura
        d = self.nit_factura.toPlainText()

        #fecha factura
        e = self.fecha.toPlainText()

        #producto para factura
        f = self.producto_para_factura.toPlainText()

        #cantidad de producto
        g = self.cantidad_producto.toPlainText()

        
        conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

        #cursor para hacer operaciones en la database
        cur = conn.cursor()
            
        cur.execute("SELECT * FROM Productos WHERE id_producto = '{}';".format(f))
        conn.commit()

        rows = cur.fetchall()

        for data in rows:
                fila = (str(data[0]), str(data[1]), str(data[2]))
                global enviarTotal
                enviarTotal = enviarTotal + ( float(data[2]) * int(g) )
                contador = int(g)
                while contador > 0:
                    productosTabla.append(fila)
                    contador -= 1


        
        texto = str(enviarTotal)
        self.total_ventas.setText("Q" + texto)

        conn.close()

        self.tabla_cliente.clearContents()

        row = 0

        for edian in productosTabla:
            self.tabla_ventas.setRowCount(row + 1)

            self.tabla_ventas.setItem(row, 0, QTableWidgetItem(edian[0]))
            self.tabla_ventas.setItem(row, 1, QTableWidgetItem(edian[1]))
            self.tabla_ventas.setItem(row, 2, QTableWidgetItem(edian[2]))

            row += 1

        print(":V")

    def borrarVentas(self):
        global enviarTotal
        global productosTabla
        productosTabla = []
        enviarTotal = 0.00
        self.total_ventas.setText("Q0.00")

        self.tabla_ventas.clearContents()

    def finalizarVentas(self):
        #id factura
        a = int(self.id_factura.toPlainText())

        #nombre para factura 
        b = self.nombre_para_factura.toPlainText()

        #direccion factura
        c = self.direccion_factura.toPlainText()

        #nit para factura
        d = self.nit_factura.toPlainText()

        #fecha factura
        e = self.fecha.toPlainText()

        #producto para factura
        f = self.producto_para_factura.toPlainText()

        #cantidad de producto
        g = self.cantidad_producto.toPlainText()

        global productosTabla
        global enviarTotal

        
        conn = psycopg2.connect("dbname=proyecto2 user=postgres password={}".format(claveBD))

        #cursor para hacer operaciones en la database
        cur = conn.cursor()

        descripcion = "a"
        cur.execute("INSERT INTO factura(id_factura, nombre, nit, descripcion, fecha, total) VALUES ( \
            {}, \
            '{}', \
            '{}', \
            '{}', \
            current_timestamp, \
            {});".format(a, b, d, descripcion, enviarTotal))

        for producto in productosTabla:
            
            cur.execute("INSERT INTO linea_factura(nombre, nit, direccion, id_factura, id_producto, cantidad, precio) VALUES( \
                '{}', \
                '{}', \
                '{}', \
                {}, \
                '{}', \
                {}, \
                {} \
                );".format(b, d, c, a, f, g, producto[2]))
        
        cur.execute("UPDATE factura \
            SET total = {} \
            WHERE id_factura = {};".format(enviarTotal, a))

        conn.commit()
        conn.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

