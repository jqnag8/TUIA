#! /bin/bash

read -p "Ingrese la contraseña: " CONTRASENA

CANTIDAD_CARACTERES=$(echo "$CONTRASENA" | wc -m)
CANTIDAD_MAYUSCULAS=$(echo "$CONTRASENA" | grep -Eco "[A-Z]" )
CANTIDAD_DIGITOS=$(echo "$CONTRASENA" | grep -Eco "[0-9]" )
CANTIDAD_MINUSCULAS=$(echo "$CONTRASENA" | grep -Eco "[a-z]")


if [ "$CANTIDAD_CARACTERES" -gt 8 ] && [ "$CANTIDAD_DIGITOS" -gt 0 ] && [ "$CANTIDAD_MAYUSCULAS" -gt 0 ] && [ "$CANTIDAD_MINUSCULAS" -gt 0 ];
then
    echo "Contraseña válida"
else
    echo "Contraseña no válida"
fi

exit 0
