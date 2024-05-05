# Parte II (Manejo de Bash)

## Ejercicios de Unidad 6

### Comandos Básicos

#### Introducción

##### 6.11

* `date` muestra la fecha y horario de hoy.
* `cal` muestra un calendario resaltando la fecha de hoy (`ncal` muestra otro layout, marcando el día de la semana.


##### 6.12

* __CTRL-A__: inicio del comando.
* __CTRL-E__: fin del comando.
* __CTRL-K__: elimina de atras para adelante, hasta la posicion del puntero.
* __ALT-D__:  elimina palabras.
* __CTRL-W__: Opuesto a CTRL-K, elimina de adelante hacia atras.



#### Sistema de Archivos

##### 6.43

* `-g` muestra la lista sin el apartado de dueño.
* `-f` muestra el contenido de los directorios de manera recursiva.
* `-t` ordena por fecha de crecion.
* `-s` ordena por tamaño de uso en disco.


##### 6.44

`cd /bin` → `ls -h`


##### 6.45 

`stat` es un comando que imprime por pantalla las propiedades de uns sistema de archivos o un archivo.


##### 6.46

El comando `cd carpeta` da error porque _carpeta_ es un archivo, no un directorio. 
Al usar `ls -log` vemos que en el apartado de los permisos, _carpeta_ resulta `-rw-r--r--`, siendo el primer símbolo un "-" refiriendose a que es un archivo. Para que sea directorio, debe imprimir "d" como primer símbolo.


##### 6.47

En total hay 3 carpetas (ocultas por empezar con ".").


##### 6.48

En el caso de que exista una directorio la fecha y horario de hoy.
* `cal` muestra un calendario resaltando la fecha de hoy (`ncal` muestra otro layout, marcando el día de la semana.


##### 6.49

`mkdir prueba` → `rmdir prueba` 
 

##### 6.50

El error surge por el hecho de querer eliminar un directorio no vacío con un comando que __solo__ elimina directorios vacíos. 

Una solución a esto podría ser:
```
mkdir carpeta
touch carpeta/archivo
rm -r carpeta
```


##### 6.51

El error surge a partir de querer eliminar un archivo con el comando `rmdir`, el cual solo elimina directorios vacíos.

Una solución a esto puede ser lo siguiente:

```
mkdir carpeta
rmdir carpeta
```


##### 6.52

El error está en intentar crear un directorio vacío dentro de un directorio que no existe. 

Una Solución puede ser:

```
mkdir carpeta1
mkdria carpeta1/carpeta2
```


##### 6.53

El comando fue:
`rm archivo`


Para evitar la confirmación se podría usar el comando 
`rm -f archivo`



##### 6.54

```
mkdir cuartos
cd cuartos
touch argentina
mkdir francia
mkdir semi1
touch semi1/argentina
touch semi1/croacia
mkdir semi2
touch semi2/francia
touch semi2/marruecos
tree
```


##### 6.55

```
mkdir directorio_nuevo
cd /.../cuartos/
cp argentina /.../directorio_nuevo/argentinav2
cp francia /.../directorio_nuevo/franciav2
cp -r semi1 /.../directorio_nuevo/semi1v2
cp -r semi2 /.../directorio_nuevo/semi2v2
```


##### 6.56

`rm -rf directorio_nuevo cuartos`

##### 6.57

- `-u` copia solo cuando el archivo fuente es mas nuevo que el destino o cuando el destino esta perdido.

- `-b` como backup, pero no admite argumentos.

##### 6.58

`readlink` imprime el valor de un enlace simbolico o duro.


##### 6.59

Montaje del pendrive:
```
lsblk
mkdir /home/_usr_/Desktop prueba
mount /dev/sdb1 /home/_usr_/Desktop/prueba
```
Desmontaje del pendrive:
```
umount /home/_usr_/Desktop/prueba
```

##### 6.60

Para buscar archivos modificados la seman pasada, se puede utilizar la opción `-mtime`.

`find -type f -mtime -7`

Siendo `-7` la opción que indica que debe buscar archivos que tengan una modificación menor a 7 días.


##### 6.61

???


##### 6.62

`rm *.*{#,~}`


##### 6.63

Elimina todos los archivos con la extensión `.txt`


##### 6.64

```
cd /bin
ls ??
ar  bc  cp  dd  du  ex  hd  ip  ln  ls  mv  nl  od  ps  sg  ss  tr  ul  wc
as  cc  dc  df  ed  gs  id  ld  lp  mt  nc  nm  pr  rm  sh  su  ua  vi  xz
```


##### 6.65

`touch {1..30}-{1..12}`


##### 6.66

El error está en que el comando `rm` no eliminó el archivo .archivo2 porque está oculto.

Una solución a esto es:
```
rm .archivo2
```
Indicando que borre el archivo oculto


##### 6.67

El comando que nos permite ver archvos ocultos en un directorio es `ls -a`


##### 6.68

* `pushd` Agrega sistemas de archivos al stack
* `popd` Elimina el primer sistema de archivos del stack
* `dirs` Invierte el stack



#### Contenido y Filtros

##### 6.93

```
nano archivo.txt
(se gurdan los cambios con CTRL-O, luego salimos con CTRL-X)
cat archivo.txt
```

##### 6.94

* Empezar por final puede ser confuso.
* No tener algún tispo de índice para buscar lo requerido, sin tener que scrollear un archivo entero.
Falta propuesta de solución

##### 6.95

`head --lines=-3 archivo.txt`


##### 6.96

```
touch archivo.txt
tail -f archivo.txt
```

Luego hago cambios de ese archivo con otra aplición, y cuando guardo los cambios, aparecen en la terminal.


##### 6.97

El comando `uniq` no muestra palabras repetidas porque las líneas repetidas no son consecutivas.


###### 6.98

No entendí como funciona strings. Devuelve texto sin sentido. Si uso `file` si puede ver la cámara.

###### 6.99

Al usar 

`file hello_world.py`

Retorna que es un archivo de tipo ASCII. Luego, al agregar "#!/bin/python", retorna que es 
script de Python y que es un archivo ASCII ejecutable.

##### 6.100

?????????????????'


