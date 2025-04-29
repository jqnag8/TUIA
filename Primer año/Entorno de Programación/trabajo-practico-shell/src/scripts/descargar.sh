#!/bin/bash
descarga_imagen(){
  # Descarga la imagen de una url que recibe como argumento
  wget -qO imagen "$1"
}

echo "Descargando imágenes..."
descarga_imagen https://image.pollinations.ai/prompt/"$1" || descarga_imagen https://random-image-pepebigotes.vercel.app/api/random-image || descarga_imagen https://fastly.picsum.photos/id/757/512/512.jpg?hmac=EYtomGDzqY6TRcz8cuzMI6I8_JnGh9BoFC2FaQrYcyE || descarga_imagen https://source.unsplash.com/random/ # Si recibe un argumento, descargará la imagen según el argumento.


if [ $? -eq 0 ]; then
  mv imagen "$(sha256sum imagen | cut -d " " -f 1)".jpg
  echo "Descarga completada." && exit 0
else
  echo "Falló la descarga." && exit 1
fi

# Este script debe descargar una sola imagen desde internet en la carpeta actual # HECHO
# Puede recibir un argumento opcional indicando la clase de la imagen. # HECHO
# El nombre del archivo deberá ser su suma de verificación y debe terminar en .jpg # HECHO
# Asegúrese de devolver un valor de salida acorde a la situación. # HECHO
# TODO redireccionar las descargas a carpeta imágenes con Docker # HECHO
