CREATE DATABASE EJ3_P2;

USE EJ3_P2;

CREATE TABLE COMPUTADORA(
	id_computadora INT IDENTITY(1,1),
	codigo INT NOT NULL,
	ram INT NOT NULL,
		CONSTRAINT PK_id_computadora_COMPUTADORA PRIMARY KEY (id_computadora),
		CONSTRAINT UQ_codigo_DOCENTE UNIQUE (codigo),
);

CREATE TABLE DOCENTE (
	id_docente int IDENTITY(1,1),
	dni int NOT NULL,
	nombre varchar(80) NOT NULL,
	apellido varchar(80) NOT NULL,
	fecha_nacimiento DATE,
	id_computadora int,
		CONSTRAINT PK_id_docente_DOCENTE PRIMARY KEY (id_docente),
		CONSTRAINT UQ_dni_DOCENTE UNIQUE (dni),
		FOREIGN KEY (id_computadora) REFERENCES COMPUTADORA(id_computadora)
);


CREATE TABLE DISCO_RIGIDO (
	id_disco int IDENTITY(1,1),
	marca varchar(50) NOT NULL,
	capacidad INT NOT NULL,
	id_computadora INT,
		CONSTRAINT PK_id_disco_DISCO_RIGIDO PRIMARY KEY (id_disco),
		FOREIGN KEY (id_computadora) REFERENCES COMPUTADORA(id_computadora)
);


CREATE TABLE TALLER (
	id_taller int IDENTITY(1,1),
	nombre varchar(80) NOT NULL,
	duracion INT NOT NULL,
	id_docente INT,
		CONSTRAINT PK_id_taller_TALLER PRIMARY KEY (id_taller),
		FOREIGN KEY (id_docente) REFERENCES DOCENTE(id_docente)
);


CREATE TABLE ESCUELA (
	id_escuela INT IDENTITY(1,1),
	nombre VARCHAR(80) NOT NULL,
		CONSTRAINT PK_id_escuela_ESCUELA PRIMARY KEY (id_escuela),
		CONSTRAINT UQ_nombre_ESCUELA UNIQUE (nombre)
);

CREATE TABLE ESCUELA_TALLER(
	id_escuela_taller INT IDENTITY(1,1),
	id_taller INT NOT NULL,
	id_escuela INT NOT NULL,
		CONSTRAINT PK_id_escuela_taller_ESCUELA_TALLER PRIMARY KEY (id_escuela_taller),
		FOREIGN KEY (id_taller) REFERENCES TALLER(id_taller),
		FOREIGN KEY (id_escuela) REFERENCES ESCUELA(id_escuela)
);


CREATE TABLE RECURSO(
	id_recurso INT IDENTITY(1,1),
	nombre VARCHAR(50) NOT NULL,
		CONSTRAINT PK_id_recurso_RECURSO PRIMARY KEY (id_recurso)
);


CREATE TABLE TALLER_RECURSO(
	id_taller_recurso INT IDENTITY(1, 1),
	id_taller INT NOT NULL,
	id_recurso INT NOT NULL,
		CONSTRAINT PK_id_taller_recurso_TALLER_RECURSO PRIMARY KEY (id_taller_recurso),
		FOREIGN KEY (id_taller) REFERENCES TALLER(id_taller),
		FOREIGN KEY (id_recurso) REFERENCES RECURSO(id_recurso)
);

CREATE TABLE APLICACION(
	id_aplicacion INT IDENTITY(1, 1),
	nombre VARCHAR(80) NOT NULL,
	_version FLOAT NOT NULL,
	distribuidor VARCHAR(80) NOT NULL,
	capacidad INT NOT NULL,
		CONSTRAINT PK_id_aplicacion_APLICACION PRIMARY KEY (id_aplicacion)
);


CREATE TABLE INSTALADOR(
	id_instalador INT IDENTITY(1, 1),
	id_computadora INT NOT NULL,
	id_aplicacion INT NOT NULL,
		CONSTRAINT PK_id_instalador_INSTALADOR PRIMARY KEY (id_instalador),
		FOREIGN KEY (id_computadora) REFERENCES COMPUTADORA(id_computadora),
		FOREIGN KEY (id_aplicacion) REFERENCES APLICACION(id_aplicacion)
);



