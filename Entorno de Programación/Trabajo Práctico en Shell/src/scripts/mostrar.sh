#!/bin/bash

# Este script es un programa interactivo que no recibe argumentos.
# Debe preguntarle al usuario que etiqueta desea buscar y mostrar por
# pantalla todas las imágenes que tengan esa etiqueta.
PS3="Elija alguna de las etiquetas: "

select etiqueta in "Todas" "Salir" "Dog" "Person" "Cat" "No Detections" "Cancelar"
do
    case $REPLY in
        1)
            for imagen in ./*.jpg; do
                echo "$imagen:"
                jp2a --colors "$imagen"
            done
            ;;
        2)
            exit 0 ;;
        *)
            echo "Opción incorrecta" ;;
    esac
etiqueta_formateada=$(echo "$etiqueta" | tr '[:upper:]' '[:lower:]') # Edita la etiqueta para que sea toda en minúsculas.
lista_resultados=$(grep -l "$etiqueta_formateada" ./*.tag)

for etiqueta in $lista_resultados; do
imagen_formateada=$(basename "$etiqueta" .tag).jpg # Le quita la extensión .tag a 'etiqueta' y la reemplaza por .jpgj

echo "$imagen_formateada:"
jp2a --colors "$imagen_formateada"
done

done
