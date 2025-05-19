#! /bin/bash

read -p "Ingrese la contraseña: " CONTRASENA

CANTIDAD_CARACTERES=`echo $CONTRASENA | wc`
CANTIDAD_MAYUSCULAS=`echo $CONTRASENA | grep -Eco "[A-Z]"`
CANTIDAD_DIGITOS=`echo $CONTRASENA | grep -Eco "[[:digit:]]"`
CANTIDAD_MINUSCULAS=`echo $CONTRASENA | grep -Eco "[a-z]"`


if [ $CANTIDAD_CARACTERES -gt 0 ] && [ $CANTIDAD_DIGITOS -gt 0 ] && [ $CANTIDAD_MAYUSCULAS -gt 0 ] && [ $CANTIDAD_MINUSCULAS -gt 0 ]; then
    echo "Contraseña válida"
else
    echo "Contraseña no válida"
fi
