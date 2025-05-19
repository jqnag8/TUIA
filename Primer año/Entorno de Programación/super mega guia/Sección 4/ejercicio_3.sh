#!/bin/bash

test -d "$1" && find "$1" -maxdepth 1 -type f | wc -l || echo "Directorio no válido"

exit 0
