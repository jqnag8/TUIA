#! /bin/bash

PS_PID=$(ps | grep "bash" | cut -d " " -f 3)

echo "$PS_PID $$"
if [ $PS_PID -eq $$ ]; then
  echo "Los PID coinciden"
else
  echo "No son idénticos"
fi 
