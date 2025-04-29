#!/bin/bash

read -p "Igrese la etiqueta que desea mostrar: " Etiqueta

archivo=$(grep -l "$Etiqueta" ./*.tag)

for imagenes in $archivo; do
    Nombre="$(echo $imagenes | cut -d "/" -f 2 | cut -d "." -f 1).jpg"
    jp2a --colors --invert -b $Nombre
done


# Este script es un programa interactivo que no recibe argumentos.
# Debe preguntarle al usuario que etiqueta desea buscar y mostrar por
# pantalla todas las imágenes que tengan esa etiqueta.
