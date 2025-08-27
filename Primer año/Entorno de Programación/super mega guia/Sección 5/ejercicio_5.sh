#! /bin/bash

if [ -e "$1" ]
then
    echo "El archivo existe"
    exit 0
else
    echo "El archivo no existe"
    exit 1
fi
