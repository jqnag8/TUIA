#!/bin/bash

TIPO_ARCHIVO=`stat -c %F $1`

if [ $? -eq 0 ]; then
    echo "El tipo de archivo es: $TIPO_ARCHIVO"
else
    echo "Error al obtener el tipo de archivo"
fi
