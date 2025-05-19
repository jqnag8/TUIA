#!/bin/bash

([ -e "$1" ] && (echo "El archivo existe" ; exit 0)) || (echo "El archivo no existe" ; exit 1)
