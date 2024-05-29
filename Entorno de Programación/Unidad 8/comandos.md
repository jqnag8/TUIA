# Unidad 8: Shell Scripting 

## Introducción

### Ejercicio 8.4
```
  touch script.py
  chmod +x script.py
  /.script.py
```
* **Observación**: agregar shebang, si no, no funcionará.

### Ejercicio 8.8

La variable *CDPATH* guarda una lista de directorios que el comando `cd` usará para encontrar la ruta al directorio a la que el usuario quiere cambiar.


### Ejercicio 8.9

```
echo $$
ps
```

* verificar si los *PID* de los emuladores de terminal son iguales 


### Ejercicio 8.16

`PS1="\w >"`

* *\w* muestra el directorio actual

### Ejercicio 8.38

`echo $PATH | tr ':' '\n'

### Ejercicio 8.39

`find -type f -exec du -h {} \; | sort | tail -n 1`


### Ejercicio 8.40


