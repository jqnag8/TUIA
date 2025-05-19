#! /bin/bash

[ $(($1 % 2)) -eq 0 ] && echo "El número es par" || echo "El número es impar"
