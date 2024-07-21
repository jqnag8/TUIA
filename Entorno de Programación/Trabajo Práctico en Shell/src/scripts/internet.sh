#!/bin/bash
echo "Verificando conexión a internet..."
PORCENTAJE_PAQUETES=$(ping -qc 5 localhost | grep -Eo "[0-100]%") # toma el resultado del porcentaje de los paquetes recibidos

if [ "$PORCENTAJE_PAQUETES" != "0%" ]; then # 0% significa que que no se perdió ningún paquete
  echo "Falló la conexión" && exit 1
else
  echo "Conexión establecida" && exit 0
fi
  
# Este script simplemente debe chequear que haya conexión a internet. # hecho
# Asegúrese de retornar un valor de salida acorde a la situación. # hecho
# Puede que necesite modificar el archivo Dockerfile. # hecho
