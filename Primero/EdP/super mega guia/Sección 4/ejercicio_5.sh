#! /bin/bash

read -rp "Ingrese un número: ('x' para terminar) " input

while [[ (! $input = 'x') && ($input -gt 0) ]]; do
    factorial=1

    for i in $(seq 1 "$input"); do
        factorial=$((factorial * i))
    done

    echo "El factorial de $input es: $factorial"
    read -rp "Ingrese un número: ('x' para terminar) " input
done

exit 0
