#! /bin/bash

[ -e "$1" ] && wc -l "$1" || exit 1

exit 0
