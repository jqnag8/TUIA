#! /bin/bash

grep -Eo '^[[:digit:]]*' archivo.txt | tr '\n' '+' | cut -d + -f 1-3 | bc
