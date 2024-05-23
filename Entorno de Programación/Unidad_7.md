# Unidad 7: Comandos Avanzados
## Usuarios, grupos y permisos
### Ejercicio 7.14

`chmod a+u *.py`

### Ejercicio 7.15

`chmod a+r *.txt`

### Ejercicio 7.16

`chmod 000 *.key`

### Ejercicio 7.17

El comando no funcina porque no tenemos los permisos de administrador.
Para solucionarlo, se puede hacer

`sudo useradd visitante`

### 7.18

`sudo usermod -s bash visitante`

### 7.19

`ll / | grep -E "^........w"`

Usamos `ll` para listar todos los archivos de la carpeta raíz de forma extensa. Luego, el resultado es ingresado a `grep` para que filtre los archivos los cuales Visitante puede escribir mediante una expresion regular

* Expresión Regular: indicamos ^ para que busque al inicio de la línea. Luego cada . equivale a un símbolo o letra que determina el tipo de archivo o permisos. Finalmente indicamos una 'w' para indicar que queremos que en los permisos de usuario esté habilitada la escritura de archivos. 



### 7.20

`useradd -m visitante`

La opción `-m` hace que el comando cree un directorio Home de forma automática

### 7.21

?????


## Procesos y Tareas

### Ejercicio 7.27

1. `sleep 1d`

2. En otra terminal, ejecutamos`htop` o `top` para luego buscar el PID del proceso sleep. Una vez encontrado (4873),

3. `kill -SIGTSTP 4873`

4. Volvemos a la terminal anterior, y ejecutamos `jobs` para ver que efectivamente el proceso está detenido.

5. Para reanudar el proceso, usamos el comando `kill -SIGCONT 4873`

6. Para interrumpir el proceso, usamos `kill -SIGTINT 4873`

### Ejercicio 7.28

```
firefox &
ps
disown 6795
```

1. & indica que lo ejecute en segundo plano
2. `ps` para mostrar información acerca de los procesos en segundo plano
3. Le pasamos al comando `disown` el PID del proceso firefox para eliminar la asociación del comando `firefox` en la sesión de shell actual.
 

## Gestión

### Ejercicio 7.34

Los comandos son Built-in de Bash, por lo tanto no existe algún archivo ejecutable que el comando `which` pueda encontrar.


### Ejercicio 7.35

* `tldr` funciona similar a `man` pero intenta ser más explicativo, dando ejemplos de uso.
* `shellcheck` verifica si un archivo .sh (shell script) tiene errores.

### Ejercicio 7.36

`neofetch` es un script personalizable que muestra información del sistema.

### Ejercicio 7.37

```
  sudo apt remove neofetch
  which neofetch
```

1. Removemos el comando `neofetch` con permisos de administrador.
2. Verificamos si existe la ruta donde se almacena el comando con `which`.

### Ejercicio 7.38

????


### Ejercicio 7.39

* `uptime` imprime cuánto tiempo estuvo prendido el sitema.
* `uname` imprime información del sistema.

## Compresión y Backup

### Ejercicio 7.50

* `zip` se usa para empaquetar y comprimir archivos.
* `unzip` se usa para descomprimir, listar o comprobar archivos .zip.
 
### Ejercicio 7.51

**Bomba Zip** es una un archivo malicioso que pretende romper el algortimo de compresión de `zip`, guardando grandes cantidades de datos.

Bombas Zip hechas por *David Fifield*:
* zbsm.zip, con un tamaño de 5.5 GB comprimidos en un archivo de 42 KB.
* zblg.zip, con un tamaño de 281 TB comprimidos en un archivo de 10 MB.
* zbxl.zip, con un tamaño de 4.5 PB comprimidos a través del algoritmo Zip64 en un archivo de 46 MB.

**(EJECUTAR EN UNA MÁQUINA VIRTUAL!!)** Usamos lUbuntu para ejecutar la bomba zip. Descargamos la [bomba zip de tamaño 281TB en un archivo de 10mb](https://www.bamsoftware.com/hacks/zipbomb/).

`cd /ruta/de/descarga && unzip zblg.zip`

* Usamos && para ejecutar los comandos en simultáneo.

## Otros Comandos

### Ejercicio 7.61

Crear un alias mediante el comando alias es crear un atajo de un comando en concreto de forma temporal. Mientras que un enlace a un archivo, es un acceso directo que puede estar en cualquier parte del sistema de archivos, permitiendonos acceder al archivo que apunta.

### Ejercicio 7.62

El comando `type` muestra el tipo de comando que se le ingresa.

* `which ls` imprime la ruta de instalación del comando.
* `type ls` imprime el tipo de comando que es `ls` (alias de `ls --color=auto`).

### Ejercicio 7.63

* **Tiempo real**: en ambos casos son parecidos.
* **Tiempo de usuario**: el tiempo de usuario es de 0 con el comando `time sleep`. En cambio, con `python3` el tiempo es similar al tiempo real.
* **Tiempo de sistema**: en ambos casos es casi nulo

### Ejercicio 7.64

`watch cat archivo.txt`

* De esta forma, `cat archivo` será ejecutado cada dos segundos, permitiendonos ver el estado del contenido de archivo.txt.

### Ejercicio 7.65

?????


### Ejercicio 7.66

