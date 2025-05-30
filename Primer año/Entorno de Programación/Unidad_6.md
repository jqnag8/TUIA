# Unidad 6: Comandos Básicos


## Introducción 

### 6.11 

* `date` muestra la fecha y horario de hoy. 
* `cal` muestra un calendario resaltando la fecha de hoy (`ncal` muestra otro layout, marcando el día de la semana). 

### 6.12 

* __CTRL-A__: inicio del comando. 
* __CTRL-E__: fin del comando. 
* __CTRL-K__: elimina de atras para adelante, hasta la posicion del puntero. 
* __ALT-D__:  elimina palabras, desde la posicion del puntero hasta el final de la palabra. 
* __CTRL-W__: Similar a ALT-D, elimina desde la posicion del puntero hasta el inicio de la palabra.


## Sistema de Archivos 

### 6.43 

* `-g` muestra la lista sin el apartado de dueño. 
* `-f` muestra el contenido de los directorios de manera recursiva. 
* `-t` ordena por fecha de crecion. 
* `-s` ordena por tamaño de uso en disco. 


### 6.44 

`ls -h /bin`
* La carpeta /bin guarda el binario de todos los comandos


### 6.45 

`stat` es un comando que imprime por pantalla las propiedades de uns sistema de archivos o un archivo.


### 6.46

El comando `cd carpeta` da error porque _carpeta_ es un archivo, no un directorio. 
Al usar `ls -log` vemos que en el apartado de los permisos, _carpeta_ resulta `-rw-r--r--`, siendo el primer símbolo un "-" refiriendose a que es un archivo. Para que sea directorio, debe imprimir "d" como primer símbolo.


### 6.47

En total hay 3 carpetas (ocultas por empezar con ".").


### 6.48

En el caso de que exista un directorio con el nombre "cd"


### 6.49

`mkdir prueba` → `rmdir prueba` 
 

### 6.50

El error surge por el hecho de querer eliminar un directorio no vacío con un comando que __solo__ elimina directorios vacíos. 

Una solución a esto podría ser:
```
mkdir carpeta
touch carpeta/archivo
rm -r carpeta
```


### 6.51

El error surge a partir de querer eliminar un archivo con el comando `rmdir`, el cual solo elimina directorios vacíos.

Una solución a esto puede ser lo siguiente:

```
mkdir carpeta
rmdir carpeta
```


### 6.52

El error está en intentar crear un directorio vacío dentro de un directorio que no existe. 

Una Solución puede ser:

```
mkdir carpeta1
mkdir carpeta1/carpeta2
```


### 6.53

El comando fue:
`rm archivo`


Para evitar la confirmación se podría usar el comando 
`rm -f archivo`



### 6.54

```
mkdir cuartos
cd cuartos
touch argentina
touch francia
mkdir semi1
touch semi1/argentina
touch semi1/croacia
mkdir semi2
touch semi2/francia
touch semi2/marruecos
tree
```


### 6.55

```
mkdir directorio_nuevo
cp -r /.../cuartos /.../directorio_nuevo
```


### 6.56

`rm -rf directorio_nuevo cuartos`

### 6.57

- `-u` copia solo cuando el archivo fuente es mas nuevo que el destino o cuando el destino esta perdido.

- `-b` como backup, pero no admite argumentos.

### 6.58

`readlink` imprime el valor de un enlace simbolico o duro.


### 6.59

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

### 6.60

Para buscar archivos modificados la seman pasada, se puede utilizar la opción `-mtime`.

`find -type f -mtime -7`

Siendo `-7` la opción que indica que debe buscar archivos que tengan una modificación menor a 7 días.


### 6.61

`find -empty d -exec cp -r {} {}-copia \;`

### 6.62

`rm *.*{#,~}`


### 6.63

Elimina todos los archivos con la extensión `.txt`

### 6.64

```
cd /bin
ls ??
```


### 6.65

`touch {1..30}-{1..12}`


### 6.66

El error está en que el comando `rm` no eliminó el archivo .archivo2 porque está oculto.

Una solución a esto es:
```
rm .archivo2
```
Indicando que borre el archivo oculto


### 6.67

El comando que nos permite ver archvos ocultos en un directorio es `ls -a`


### 6.68

* `pushd` Agrega sistemas de archivos al stack
* `popd` Elimina el primer sistema de archivos del stack
* `dirs` Invierte el stack



## Contenido y Filtros

### 6.93

```
nano archivo.txt
(se gurdan los cambios con CTRL-O, luego salimos con CTRL-X)
cat archivo.txt
```
### 6.94

* Empezar por final puede ser confuso.
* No tener algún tispo de índice para buscar lo requerido, sin tener que scrollear un archivo entero.
Falta propuesta de solución

### 6.95

`head --lines=-3 archivo.txt`


### 6.96

```
touch archivo.txt
tail -f archivo.txt
```

Luego hago cambios de ese archivo con otra aplición, y cuando guardo los cambios, aparecen en la terminal.


### 6.97

El comando `uniq` no muestra palabras repetidas porque las líneas repetidas no son consecutivas.


### 6.98

No entendí como funciona strings. Devuelve texto sin sentido. Si uso `file` si puede ver la cámara.

### 6.99

Al usar 

`file hello_world.py`

Retorna que es un archivo de tipo ASCII. Luego, al agregar "#!/bin/python", retorna que es 
script de Python y que es un archivo ASCII ejecutable.

### 6.100

```
touch archivo.txt
(Se edita el archivo)
cut -d ',' -f 2 archivo.txt
```

De esa forma, devuelve el segundo campo del archivo, que son las marcas.


### 6.101

* `comm` compara los datos de dos archivos ordenados en formato de columnas 
(1 = datos de FILE1, 2 = FILE2, 3 = FILE1 y FILE2).
* `diff` similar a comm. Compara dos o más archivos que no necesariamente deben estar ordenados.

### 6.102

1. `(x|y)(x)`
2. `x{2}`
3. `^(x{2})*$`
4. `^(x{1})*$`

(Sin Terminar)

### 6.103

`grep .*[^;]$`

### 6.104

* `-A` Imprime _n_ líneas de texto después de las líneas concidentes.
* `-B` imprime _n_ líneas de texto antes de las líneas coincidentes.

### 6.105

El comando `nl` recibe un archivo como argumento y devuelve el contenido con las líneas enumeradas como salida estandar.


### 6.106

El comando `fold` toma como argumento un archivo y devuelve el texto con las 
líneas ajustadas a un ancho determinado como salida estandar


## Secuenciación, redirección y tuberías

### 6.120

* `true` devuelve un valor de true. Se utiliza para dar a entender que algún comando terminó con exito.
*  `false` devuelve un valor false. Retorna error para algún proceso.

`(true && false) || echo "el comando no se ejecutó"`

### 6.121

`cat * | tee log.txt`

Solución alternativa: `find -type f -exec cat {} \; > archivo.txt`

### 6.122

imprime por pantalla un 2 seguido de los archivos del directorio y al final, un 3. 
Luego guarda la salida en un archivo llamado 10

### 6.123

`<` toma los datos de un archivo para luego pasarlos como argumentos de un comando.

`cat < archivo1 > archivo2` guarda el contenido de archivo1 en archivo2.

### 6.124

`> archivo.txt`


### 6.125

`echo {a..z}{a..z}{a..z}{a..z} > archivo.txt`

**Peso** = 2.2Mb


### 6.126

(buscar un directorio con archivos .jpg)

`find / -type f -name *.jpg > archivo.txt`


### 6.127

```
echo {0..9}{0..9} > archivo.txt
**Para devolver el máximo:**
cat archivo.txt | tr ' ' '\n' | head -n 1
**Para devolver el mínimo**
cat archivo.txt | tr ' ' '\n' | tail -n 1
```

### 6.128

Se crea un archivo con más de 3 líneas...

`cat -n archivo.txt | grep 3`

### 6.129

`find /ubicacion/de/directorio -type f -exec wc -l {} + | sort | tail -n 1`

### 6.130

`find -type d | wc -l`

### 6.131

?????

### 6.132

?????

### 6.133

`history | grep cd | wc -l`

### 6.134

`ls /usr/share/doc | grep GNU | wc -l`

### 6.135

`(echo "primera linea" ; cat archivo.txt) | tee archivo.txt`

### 6.136

1. Shell ejecutará a, b, e, f (4).
2. Shell ejecutará a, b, c, d, f (5).
3. Shell ejecutará a, b, c, e y f (5).
