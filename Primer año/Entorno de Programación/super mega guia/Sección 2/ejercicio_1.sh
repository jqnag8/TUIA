#!/bin/bash

if [ $(( $1 % $2 )) -eq 0 ]; then
    echo "$1 es divisible por $2"
else
    echo "$1 no es divisible por $2"
fi

exit 0
