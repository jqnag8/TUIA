#! /bin/bash

SECUENCIA_NUMEROS=$(seq -s " " 0 2 30)

for i in "${SECUENCIA_NUMEROS[@]}"
do
    echo $i
done
