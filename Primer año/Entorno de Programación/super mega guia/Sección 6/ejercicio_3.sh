#! /bin/bash

if [ ! -f "$1" ]; then
    echo "File not found!"
    exit 1
fi

sort "$1" | uniq
