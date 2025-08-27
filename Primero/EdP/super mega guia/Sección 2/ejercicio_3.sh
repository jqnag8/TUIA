#!/bin/bash

if ([ $(($1 % 4)) -eq 0 ] && ! [ $(($1 % 100)) -eq 0 ]) || [ $(($1 % 400)) -eq 0 ]; then
    echo "Es bisiesto. Tiene 366 días, 8.784 horas, 5.270.400 miinutos y 31.622.400 segundos"
else
    echo "No es bisiesto. Tiene 365 días, 8.754 horas, 525.600 y 31.536.000 segundos"
fi

exit 0
