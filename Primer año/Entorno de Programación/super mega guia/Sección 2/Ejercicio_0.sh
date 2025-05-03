if [ $# -eq 0 ];then
  echo "No se ingreso ningun valor"
  
else
  if [ $(($1 % 2)) -eq 0 ]; then
    echo "Es par"
    else
    echo "Es impar"
  fi
fi
