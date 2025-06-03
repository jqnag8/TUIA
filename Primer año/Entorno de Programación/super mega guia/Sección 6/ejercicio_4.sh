#! /bin/bash

if [ ! $# -eq 3 ]; then
    echo "Error"
    exit 1
fi

tr "$1" "$2" "$3"
