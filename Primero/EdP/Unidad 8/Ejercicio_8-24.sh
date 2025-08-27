#! /bin/bash

CHECKSUM=$(sha256sum "$1" | cut -d ' ' -f 1) # cut para quedarnos con la parte que muestra el checksum
([ "$CHECKSUM" = "$2" ] && echo "Los checksum coinciden") || echo "Los checksum no coinciden"

