#! /bin/bash

CONTRASENA=""
read -sp "Ingrese la contraseña para $USER: " CONTRASENA # Con -s, read no muestra el contenido de que se ingresa.

echo "$CONTRASENA" >> contraseñas.txt 

# TODO: agregar salto de línea
