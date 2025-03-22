#!/bin/bash

DIRECTORIO="Papelera"

(mv "$1" ~/$DIRECTORIO && echo "Finalizó con éxito") || (mkdir $DIRECTORIO && echo "Se creó el directorio") || echo "Error: el archivo no existe" 

# (sin terminar)
