#!/bin/bash

if [ ! -e "$1" ]
then
    echo "El archivo no existe"
    exit 1
fi

lineas_archivo=$(wc -l "$1" | cut -d ' ' -f 1)

echo "El archivo tiene $lineas_archivo lineas"

exit 0
