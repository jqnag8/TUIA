#! /bin/bash

read -p "Ingrese la contraseña: " CONTRASENA

CANTIDAD_CARACTERES=$(echo "$CONTRASENA" | wc -m)
CANTIDAD_MAYUSCULAS=$(echo "$CONTRASENA" | grep -Eo "[A-Z]" | wc -l)
CANTIDAD_DIGITOS=$(echo "$CONTRASENA" | grep -Eo "[0-9]" | wc -l)
CANTIDAD_MINUSCULAS=$(echo "$CONTRASENA" | grep -Eo "[a-z]" | wc -l)


if [ "$CANTIDAD_CARACTERES" -gt 8 ] && [ "$CANTIDAD_DIGITOS" -gt 0 ] && [ "$CANTIDAD_MAYUSCULAS" -gt 0 ] && [ "$CANTIDAD_MINUSCULAS" -gt 0 ];
then
    echo "Contraseña válida"
    exit 0
else
    echo "Contraseña no válida"
    exit 1
fi
