#!/bin/bash

# Este script es un programa interactivo que no recibe argumentos. # Hecho
# Debe preguntarle al usuario que etiqueta desea buscar y mostrar por # Hecho
# pantalla todas las imágenes que tengan esa etiqueta. # Hecho

read -p "Ingrese una etiqueta a buscar: " etiqueta

etiqueta_formateada=$(echo "$etiqueta" | tr '[:upper:]' '[:lower:]')

if [ "$etiqueta" == "todas" ]; then
    for imagen in ./*.jpg; do
        echo "$imagen:"
        jp2a --colors "$imagen"
    done
    exit 0
fi

lista_etiquetas=$(grep -l "$etiqueta_formateada" ./*.tag)

if [ $? -ne 0 ]; then
    echo "La etiqueta ingresada no existe." && exit 1
else
    for etiqueta in $lista_etiquetas; do
    imagen_formateada=$(basename "$etiqueta" .tag).jpg
    echo "$imagen_formateada:"
    jp2a --colors "$imagen_formateada"
    done
    exit 0
fi
