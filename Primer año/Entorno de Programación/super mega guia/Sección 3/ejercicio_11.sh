#! /bin/bash

read -p "Ingrese la contraseña: " CONTRASENA

CANTIDAD_CARACTERES=$(wc -m <<< $CONTRASENA)
CANTIDAD_MAYUSCULAS=$(grep -Eco "[A-Z]" <<< $CONTRASENA)
CANTIDAD_DIGITOS=$(grep -Eco "[0-9]" <<< $CONTRASENA)
CANTIDAD_MINUSCULAS=$(grep -Eco "[a-z]" <<< $CONTRASENA)


if [ "$CANTIDAD_CARACTERES" -gt 8 ] && [ "$CANTIDAD_DIGITOS" -gt 0 ] && [ "$CANTIDAD_MAYUSCULAS" -gt 0 ] && [ "$CANTIDAD_MINUSCULAS" -gt 0 ]

    echo "Contraseña válida"
else
    echo "Contraseña no válida"
fi

exit 0
