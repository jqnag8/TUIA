#!/bin/bash

LISTA_ARCHIVOS=$(find . -mindepth 1)

if [ -z "$LISTA_ARCHIVOS" ]; then # Se verifica si la carpeta está vacía
  echo "La carpeta está vacía. No hay nada que comprimir" && exit 1
fi

[ -e suma_ver.txt ] && rm suma_ver.txt # Borra el suma_ver.txt viejo 

[ -e backup.tar ] && rm backup.tar # Elimina el archivo de respaldo anterior si existe

tar -cf backup.tar ./*

sha256sum backup.tar > suma_ver.txt && echo "Compresión completada" && exit 0

# Este script comprime todo el contenido de la carpeta actual y además, genera # hecho
# una suma de verificación del archivo resultante en un archivo separado. # hecho