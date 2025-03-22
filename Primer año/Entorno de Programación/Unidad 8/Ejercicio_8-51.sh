#! /bin/bash 

wget #url

while [ $? -ne 0 ]; do
  echo "Reintentando descarga... "
  sleep -s 10
  wget # url
done
