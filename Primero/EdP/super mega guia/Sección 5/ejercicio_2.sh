#! /bin/bash

[ $# -lt 2 ] && echo "Error: Debe proporcionar al menos dos argumentos." >&2 && exit 1

echo $(($1 + $2))

exit 0
