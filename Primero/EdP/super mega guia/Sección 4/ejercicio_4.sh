#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Por favor, ingrese un número como argumento."
    exit 1
fi

function fibonacci() {
    if [[ $1 -eq 0 || $1 -eq 1 ]]; then
        echo "$1"
    else
        echo $(( $(fibonacci $(( $1 - 1 )) ) + $(fibonacci $(( $1 - 2 )) ) ))
    fi
}

for i in $(seq 0 "$1"); do
    fibonacci "$i"
done
