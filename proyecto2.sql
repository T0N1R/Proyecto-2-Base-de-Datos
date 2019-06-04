
CREATE TABLE productos(
	id_producto INT NOT NULL, 
	nombre VARCHAR(30) NOT NULL, 
	precio FLOAT NOT NULL, 
	PRIMARY KEY(id_producto)
	);


CREATE TABLE clientes(
	id_cliente INT NOT NULL,
	nombre VARCHAR(30) NOT NULL,
	nit VARCHAR(10) NOT NULL,
	PRIMARY KEY(id_cliente)
);


CREATE TABLE factura(
	id_factura INT NOT NULL,
	nombre VARCHAR(30) NOT NULL,
	nit VARCHAR(10) NOT NULL,
	descripcion VARCHAR(5),
	fecha timestamp NOT NULL,
	total FLOAT NOT NULL,
	PRIMARY KEY(id_factura)
);

CREATE TABLE linea_factura(id_linea_factura INT NOT NULL, id_factura INT NOT NULL, id_producto INT, cantidad INT NOT NULL, precio FLOAT NOT NULL, PRIMARY KEY(id_linea_factura), FOREIGN KEY(id_factura) REFERENCES factura(id_factura), FOREIGN KEY(id_producto) REFERENCES productos(id_producto));

select * from factura;


select * from linea_factura;

