# Respuestas práctica 0.5
### Ejercicio 0
En los dos if's, la función tendrá dos operaciones (una operacion y una asignacion). Como la cantidad de operaciones
no depende de la entrada, entonces el programa tiene O(1).

### Ejercicio 1

### Ejercicio 3
* 1 + n * 1 (linea 2)
* n * 1 * 3 = 3n (for's)
total: 1 * n * 3 = 3n -> O(n)

### Ejercicio 4
* 1 (linea 2)
* n asignaciones de i + n print's (primer for)
* m asignaciones de j + m print's (2do for)
* 3 asignaciones de k + 3 print's (3er for)

resultado: 1 + 2n * 2m * 3 = 1 + 2n * 6m = 1 + 12nm = 12 (1/12 + nm) -> O(nm)

### Ejercicio 5
* n asignaciones de i (linea 2)
* n comparacion (if) de b (linea 3)
* n print's, nm asignaciones de j, nm print's (if del primer for)
* n print's, 1000 asignacinoes de k, 1000 print's (else)

resultado: n + n + n + nm + nm + n + 1000 + 1000 = 4n + 2nm + 2000 = 4 (n + 1/2nm) + 2000 -> O(n + nm) 

### Ejercicio 6
* 1 if
* print
* 10 asignaciones de i
* 10 prints
* 1 print

resultado: 1 + 1 + 10 + 10 = 22 -> O(1)

### Ejercicio 7
* el while puede ejecutarse hasta 9999 veces
* De igual forma, sucede con el for (definimos 'n' como la longitud de lista)

resultado: 1 + 1 + n + n + n + n + n = 2 + 4n = 2 (1 + 2n) -> 1 + 2n -> O(n)

### Ejercicio 8
* while se ejecuta hasta len(L1) + len(L2) (lo llamamos 'n')
* Luego como siempre se ejecuta algun for, hay len(L2) - j (o len(L1) - i) que definimos como 'k'

resultado: O(nk)


### Ejercicio 9
* El for se ejecuta 'n' veces que sería la cantidad de elementos que hay en la diagonal de la matriz.

resultado: O(n)

### Ejercicio 10
* El for se ejecuta a lo sumo 'numero' - 1 veces.

resultado: O(n)

### Ejercicio 11
* El for se ejecuta 'numero' veces

resultado: O(n)

### Ejercicio 12
* 2 asignaciones
* 2 comparaciones
* 1 asignacion
* for se ejecuta 'numero' - 1 veces

resultado: O(n)
