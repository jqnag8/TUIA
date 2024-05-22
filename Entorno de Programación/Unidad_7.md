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

?????

### 7.20

`useradd -m visitante`

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
 



 
