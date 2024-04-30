# Parte II (Manejo de Bash)
## Ejercicios de Unidad 6

### 6.11
* `date` muestra la fecha y horario de hoy.
* `cal` muestra un calendario resaltando la fecha de hoy (`ncal` muestra otro layout, marcando el día de la semana.


### 6.12

* __CTRL-A__: inicio del comando.
* __CTRL-E__: fin del comando.
* __CTRL-K__: elimina de atras para adelante, hasta la posicion del puntero.
* __ALT-D__:  elimina palabras.
* __CTRL-W__: Opuesto a CTRL-K, elimina de adelante hacia atras.


### 6.43

* `-g` muestra la lista sin el apartado de dueño.
* `-f` muestra el contenido de los directorios de manera recursiva.
* `-t` ordena por fecha de crecion.
* `-s` ordena por tamaño de uso en disco.


### 6.44

`cd /bin` → `ls -h`


### 6.45 

`stat` es un comando que imprime por pantalla las propiedades de uns sistema de archivos o un archivo.


### 6.46

El comando `cd carpeta` da error porque _carpeta_ es un archivo, no un directorio. 
Al usar `ls -log` vemos que en el apartado de los permisos, _carpeta_ resulta `-rw-r--r--`, siendo el primer símbolo un "-" refiriendose a que es un archivo. Para que sea directorio, debe imprimir "d" como primer símbolo.


### 6.47

En total hay 3 carpetas (ocultas por empezar con ".").


### 6.48

En el caso de que exista una carpeta con el nombre "cd".


### 6.49

`mkdir prueba` → `rmdir prueba` 
 

### 6.50

El error surge por el hecho de querer eliminar un directorio no vacío con un comando que __solo__ elimina directorios vacíos. 

Una Solución a esto podría ser:
```
mkdir carpeta
touch carpeta/archivo
rm -r carpeta
```


### 6.51


