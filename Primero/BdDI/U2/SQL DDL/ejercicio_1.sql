CREATE DATABASE P2_EJ1;

USE P2_EJ1;


CREATE TABLE EMPLEADO (
	Legajo varchar(5),
	Nombre varchar(80),
	Domicilio varchar(80),
	Telefono varchar(10),
	Sector varchar(80),
	Sueldo money,
		CONSTRAINT PK_EMPLEADO_Legajo PRIMARY KEY (Legajo),
		CONSTRAINT UQ_EMPLEADO_Telefono UNIQUE (Telefono));

INSERT INTO EMPLEADO 
VALUES ('123', 'Joaquin', 'San Martín 150', '3416567209', 'Produccion', 25000)

CREATE TABLE SERVICIO_TECNICO (
	Serviciotecnicoid int IDENTITY(1,1),
	Nombre varchar(80),
	Domicilio varchar(80),
	Telefono varchar(10),
	Sector varchar(80),
	Sueldo money,
		CONSTRAINT PK_SERVICIOTECNICO_Legajo PRIMARY KEY (Serviciotecnicoid),
		CONSTRAINT UQ_SERVICIOTECNICO_Telefono UNIQUE (Telefono),
		CONSTRAINT CK_SERVICIOTECNICO_Sueldo CHECK (Sueldo > 0)
);


INSERT INTO SERVICIO_TECNICO 
VALUES ('Juan Costas', 'San Martin 100', '3416255932', 'Produccion', 100000)

SELECT * FROM SERVICIO_TECNICO