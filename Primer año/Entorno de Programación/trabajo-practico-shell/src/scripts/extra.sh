#!/bin/bash

echo "Eliminando archivos..."
sleep 5
find . -mindepth 1 ! -name  "*.md" -exec rm -rf {} +
echo "Archivos eliminados"

