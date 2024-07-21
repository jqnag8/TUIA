#!/bin/bash
if [ $# -gt 1 ] ; then
  echo "Error: Demasiados argumentos" && exit 1 # Si la función recibe más de un argumento, la descarga no se ejecutará
elif [ $# -eq 0 ]; then
  wget --output-document imagen https://random-image-pepebigotes.vercel.app/api/random-image || wget --ouput-document imagen https://fastly.picsum.photos/id/757/512/512.jpg?hmac=EYtomGDzqY6TRcz8cuzMI6I8_JnGh9BoFC2FaQrYcyE || wget --output-document imagen https://source.unsplash.com/random/ # cuando no recibe un argumento, descargará una imagen aleatoria de alguna de las páginas 
else
	wget --output-document imagen https://image.pollinations.ai/prompt/"$1" # si recibe un argumento, descargará la imagen según el argumento.
fi

if [ $? -eq 0 ]; then
  mv imagen "$(sha256sum imagen | cut -d " " -f 1)".jpg
  echo "Descarga completada" && exit 0
else
  echo "Falló la descarga" && exit 2
fi

# Este script debe descargar una sola imagen desde internet en la carpeta actual # HECHO
# Puede recibir un argumento opcional indicando la clase de la imagen. # HECHO
# El nombre del archivo deberá ser su suma de verificación y debe terminar en .jpg # HECHO
# Asegúrese de devolver un valor de salida acorde a la situación. # HECHO
# TODO redireccionar las descargas a carpeta imágenes con Docker # HECHO

