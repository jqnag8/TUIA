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

### Ejercicio 
