#!/bin/bash

read -p "Ingrese el numero: " NUMERO

suma=0

for i in $(seq 1 $NUMERO)
do
    suma=$((suma + i))
done

echo "La suma total es $suma"
exit 0
