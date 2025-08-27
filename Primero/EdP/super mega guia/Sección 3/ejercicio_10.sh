#! /bin/bash

vocales=('a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U')
consonantes=('b' 'c' 'd' 'f' 'g' 'h' 'j' 'k' 'l' 'm' 'n' 'ñ' 'p' 'q' 'r' 's' 't' 'v' 'w' 'x' 'y' 'z' 'B' 'C' 'D' 'F' 'G' 'H' 'J' 'K' 'L' 'M' 'N' 'Ñ' 'P' 'Q' 'R' 'S' 'T' 'V' 'W' 'X' 'Y' 'Z')

for letra in "${vocales[@]}"
do
    if [ $1 = $letra ]
    then
        echo "Es una vocal"
        exit 0
    fi

done

for letra in "${consonantes[@]}"
do
    if [ $1 = $letra ]
        then
            echo "Es una consonante"
            exit 0
        fi
done

echo "Valor no válido"
exit 0
