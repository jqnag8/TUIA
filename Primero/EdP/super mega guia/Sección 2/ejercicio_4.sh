#!/bin/bash

if [ -f "$1" ]; then
    if [ -x "$1" ];then
        echo "Tiene permisos de ejecución"
    else
        echo "No tiene permisos de ejecución"
    fi

    echo "----------"

    if [ -w "$1" ];then
        echo "Tiene permisos de escritura"
    else
        echo "No tiene permisos de escritura"
    fi

    echo "----------"

    if [ -x "$1" ];then
        echo "Tiene permisos de ejecución"
    else
        echo "No tiene permisos de ejecución"
    fi

else
    echo "El archivo no existe"
fi

exit 0
