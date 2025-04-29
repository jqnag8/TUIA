#!/bin/bash
listar_elementos(){
 find "$1" -type f -name "*$2" -exec basename {} "$2" \; # Recibe una ruta y una extension para obtener una lista de nombres de archivos
}

LISTA_JPG_ACTUAL=$(listar_elementos . .jpg) # Lista los .jpg dentro de .

if [ -z  "$LISTA_JPG_ACTUAL" ]; then
  echo "No existen imágenes para analizar" && exit 1
else 
  for imagen in $LISTA_JPG_ACTUAL; do
    if [ -e ./"$imagen".tag ]; then
      continue
    else
      mkdir -p ./temp ; cp ./"$imagen".jpg ./temp # Aqui se guardaran las imagenes que seran analizadas por yolo. Se crea solo si no existe.
    fi
  done
  # Generamos etiquetas
  if [ -d ./temp ] ; then
    echo "Creando etiquetas nuevas..."
    LISTA_IMAGENES_TEMP=$(listar_elementos ./temp .jpg) # lista los .jpg en /temp
  
    yolo predict source=./temp > ./temp/temp.txt
  
    for imagen in $LISTA_IMAGENES_TEMP; do
      cant_palabras=$(grep "$imagen" ./temp/temp.txt | wc -w ) # Se cuentan las palabras de la linea donde se analiza la imagen
      grep "$imagen" ./temp/temp.txt | cut -d ' ' -f 5-$((cant_palabras - 1)) > ./"$imagen".tag # Devuelve los tags
    done
    echo "Las etiquetas fueron creadas correctamente" && rm -rf ./temp && exit 0
  else 
    echo "Todas las imágenes ya están etiquetadas" && exit 2
  fi
fi


# ------ CONSIGNAS ------
# Debe crearse un archivo con el mismo nombre que la imagen, pero extensión .tag # HECHO
# donde se guardan las etiquetas. Por ejemplo, un archivo .tag podría tener:
# 2 persons, 1 potted plant, 1 laptop, 2 books # HECHO
#
# Asegúrese de devolver un valor de salida acorde a la situación. # HECHO

