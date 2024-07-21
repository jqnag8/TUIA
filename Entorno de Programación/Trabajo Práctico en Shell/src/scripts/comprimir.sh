#!/bin/bash
LISTA_ARCHIVOS=$(ls -A)

if [ -z "$LISTA_ARCHIVOS" ]; then # Se verifica si la carpeta está vacía
  echo "La carpeta está vacía. No hay nada que comprimir" && exit 1
else
  if [ -e ./suma_ver.txt ]; then
    rm suma_ver.txt  # Borra el suma_ver.txt viejo 
  elif [ -e ./backup.tar ]; then
    rm ./backup.tar # borra el ultimo .tar
  fi
    tar -cf backup.tar ./*
    sha256sum backup.tar > suma_ver.txt && echo "Compresión completada" && exit 0
fi

# Este script comprime todo el contenido de la carpeta actual y además, genera # hecho
# una suma de verificación del archivo resultante en un archivo separado. # hecho

