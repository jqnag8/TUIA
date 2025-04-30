# Sección 1

### Ejercicio 0

```bash
  echo "Hola mundo"
```

### Ejercicio 2

```bash
  chmod u+x Ejercicio_1
```

### Ejercicio 3

```bash
bash Ejercicio_1.sh # Opción 1
./Ejercicio_1.sh    # Opción 2
```

### Ejercicio 5

```bash
  echo $USER
```

### Ejercicio 6

```bash
  echo $USER > archivo.6
```

### Ejercicio 14

```bash
  echo $PATH > PATH.bkp
```

### Ejercicio 15

```bash
  mkdir -p ./bin
  "echo $USER" > ./bin/hola
  export PATH="$PATH:.bin/hola"
```

### Ejercicio 16

```bash
  bash ej.16 1> ej.16.out && ej.16.out 2> ej.16.err
```


### Ejercicio 17

```bash
  bash ej.16 > /dev/null
```
