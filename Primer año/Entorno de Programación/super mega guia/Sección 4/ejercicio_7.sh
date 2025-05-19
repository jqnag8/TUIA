#! /bin/bash

lista_astericos=()

for i in $(seq 0 3)
do
    lista_astericos[i]="*"
    echo "${lista_astericos[@]}"
done
