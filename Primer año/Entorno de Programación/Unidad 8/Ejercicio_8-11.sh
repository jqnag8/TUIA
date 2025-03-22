#!/usr/bin/bash

SUMA=$1+$2

echo "$SUMA"| bc # bc toma como entrada estandar el resultado de echo y luego ejecuta la suma
