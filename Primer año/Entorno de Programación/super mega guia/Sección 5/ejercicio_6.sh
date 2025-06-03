#! /bin/bash

if [ $# -eq 0 ]; then
    echo "Ingrese un argumento"
    exit 1
fi

for i in $(seq 0 $(( ${#1} - 1 )) ); do
    echo "${1:i:1}"
done
