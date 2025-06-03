#! /bin/bash

if [ ! $# -eq 1 ]; then
    echo "Error: Usuario no válido"
    exit 1
fi

ps -ef | grep -Ec "$1"; exit 0
