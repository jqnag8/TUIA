#!/bin/bash
echo "Verificando conexión a internet..."
ping -qc 5 google.com # envia 5 paquetes a la direccion google.com

if [ $? -eq 0 ]; then 
  echo "Conexión establecida" && exit 0
else
  echo "Falló la conexión" && exit 1
fi
  
# Este script simplemente debe chequear que haya conexión a internet. # hecho
# Asegúrese de retornar un valor de salida acorde a la situación. # hecho
# Puede que necesite modificar el archivo Dockerfile. # hecho
  
