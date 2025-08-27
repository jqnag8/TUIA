#! /bin/bash

if [ ! $# -eq 2 ]; then
    echo "Ingrese dos argumentos"
    exit 1
fi

echo $(($1 * $2)); exit 0
