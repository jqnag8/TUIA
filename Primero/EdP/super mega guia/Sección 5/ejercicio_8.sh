#! /bin/bash

if [ ! -d "$1" ]; then
    echo "Ingrese un directorio válido"
    exit 1
fi

ls "$1"; exit 0
