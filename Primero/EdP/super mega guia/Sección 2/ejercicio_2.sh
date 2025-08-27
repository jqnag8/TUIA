#!/bin/bash

if ([ $(($1 % 4)) -eq 0 ] && ! [ $(($1 % 100)) -eq 0 ]) || [ $(($1 % 400)) -eq 0 ]; then
    echo "Es bisiesto"
else
    echo "No es bisiesto"
fi

exit 0
