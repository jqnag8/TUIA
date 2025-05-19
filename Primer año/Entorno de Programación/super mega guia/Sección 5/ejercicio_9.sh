#!/bin/bash

# Este programa toma una cadena y devuelve la cadena en orden inverso

read -rp "Introduce una cadena: " cadena

longitud=${#cadena}
resultado=""

for (( i=longitud-1; i>=0; i-- ))
do
    resultado="$resultado${cadena:$i:1}"
done

echo "Cadena invertida: $resultado"
