# Trabajo Práctico de Entorno de Programación
Este repositorio es un trabajo práctico para la materia "Entorno de
Programación" de la carrera T.U.I.A. en F.C.E.I.A. (U.N.R.).

Aquí puede leerse el [enunciado](docs/enunciado.md) del trabajo.

### Dependencias

Es necesario tener instalados `docker` y `docker buildx` para poder ejecutar
este programa. En distribuciones basadas en Ubuntu esto puede conseguirse así:
```bash
sudo apt update
sudo apt install docker.io docker-buildx
```

Luego será necesario habilitar el servicio de contenedores de docker:
```bash
sudo systemctl enable docker
sudo systemctl start docker
```

También puede ser de utilidad agregar al usuario actual al grupo `docker`:
```bash
sudo usermod -aG docker $USER
```
Para que este cambio surja efecto, es necesario reiniciar la sesión.

### Ejecución

Para poder utilizar el programa primero debe construir el contendor:
```bash
docker buildx build -t entorno .
```

Luego puede ejecutarse el contenedor con el siguiente comando en la raíz del repositorio:
```bash
docker run -itv ./imagenes:/imagenes entorno
```
De esta forma, el directorio local de imagenes y el de Docker estarán sincronizados y lo que se descargue con Docker permanecerá localmente

Tambien puede correrse el programa fuera del contenedor:
```bash
./src/main.sh
```
### Explicación de scripts
- [descargar.sh](src/scripts/descargar.sh): está hecho con el propósito de descargar una imagen desde una URL y renombrarla utilizando su suma de verificación. 
Primero definimos una función llamada 'descarga_imagen' y toma una URL como argumento. La opción `-q` hace que `wget`,que descarga las imagenes de la URL, opera sin mostrar mensajes, y `-O` especifica el nombre del archivo de salida, que en este caso es `imagen`.
Luego hacemos un `echo` informando que inicia la descarga y después llamamos a la función 'descarga_imagen' pasándole varias URLs.
Después verificamos el código de salida del último comando ejecutado con el comando `$?` y si es igual a 0, se cambia el nombre de 'imagen' a la suma de verificación agregándole la extensión '.jpg'.
Por último muestra un mensaje de finalización con código de salida 0 o, en su defecto, un mensaje de error si tiene código de salida 1.

- [etiquetar.sh](src/scripts/etiquetar.sh): tiene como objetivo identificar y etiquetar imágenes en un directorio utilizando YOLO.
Definimos una función llamada 'listar_elementos' en la que utilizamos el comando `find` para localizar archivos que coincidan con la extensión especificada `$2` en el directorio dado `$1`. Luego, `basename` lo usamos para eliminar la ruta del archivo y solo retornar el nombre del archivo sin la extensión.
Invocamos la funcíon anterior para una lista de todos los archivos `.jpg` que se encuentran el el directorio actual, para luego guardarlo en una variable 'LISTA_JPG_ACTUAL'.
Después verificamos si la variable es una cadena vacía con la opción `-z`, si no se encuentran archivos `.jpg` manda un mensaje de error y sale con código de salida 1.
Luego iteramos sobre 'LISTA_JPG_ACTUAL' y verificamos si ya existe un archivo de etiqueta `.tag` para la imagen, si es así el script pasa a la siguiente imagen. Si no existe la etiqueta, se crea un directorio temporal `./temp` donde se copiará la imagen.
Si se crea el directorio './temp' se le informa al usuario que se estan creando nuevas etiquetas y se guardan en una lista las imagenes '.jpg' en './temp'. Se ejecuta el comando `yolo predict` para procesar las imágenes en './temp' y se guarda la salida en './temp/temp.txt'.
Para cada imagen, se extraen las etiquetas del archivo 'temp.txt'. Se cuentan las palabras en la línea correspondiente a la imagen para determinar el rango de las etiquetas y se extraen estas etiquetas usando `cut`. Finalmente, las etiquetas se guardan en un archivo '.tag' correspondiente. Se informa al usuario que las etiquetas se crearon correctamente y se elimina el directorio temporal.
Si no se crea el dirctorio './temp' se le avisa al usuario que ya estan etiquetadas todas las imagenes.

- [mostrar.sh](src/scripts/mostrar.sh): busca etiquetas específicas en archivos '.tag' dentro del directorio actual y, en función de esas etiquetas, muestra imágenes que corresponden en formato JPG.
Primero utilizamos el comando `read` para poder solicitar a el usuario que ingrese la etiqueta que desea buscar y con la opción `-p` mostramos el texto ingresado antes que se solicite respuesta del usuario.
Luego, con el comando `grep` buscamos en los archivos el que tenga la etiqueta proporcionada con la opción `-l` para que solo devuelva los nombres de los archivos que coinciden. Los archivos buscados son aquellos con la extensión '.tag' en el directorio actual.
En las siguientes líneas hacemos que se itere sobre los archivos encontrados que se almacenaron previamente en la variable 'archivo'. Usamos `echo` y `cut` para extraer el nombre del archivo sin la ruta y sin la extensión '.tag' y luego concatenamos el '.jpg' al nombre para formar el nombre de la imágen.
Por último usamos el comando `jp2a` con las opciones `--invert` y `--colors` que configuran los colores y la opción `-b` que le da un marco blanco.

- [comprimir.sh](src/scripts/comprimir.sh): está hecha con el objetivo de comprimir todos los archivos en el directorio actual en un archivo `.tar` y generar una suma de verificación de la compresión realizada.
Primero usamos el comando `find` para buscar archivos y directorios dentro del directorio actual pero no en el directorio raíz, para eso utilizamos el comando `-mindepth 1` ya que queremos sólo el contenido del directorio actual, no la carpeta. 
Después verificamos si la carpeta estaba vacía con el comando `-z` que verifica si el resultado de `find` es una cadena vacía. Luego de esto manda un mensaje informando que la carpeta está vacía y termina la ejecución con el código de salida 1.
Luego, se verifica si el archivo 'suma_ver.txt' y 'backup.tar' existen con el comando `-e`, si es así, se eliminan para evitar conflictos.
Creamos un nuevo archivo .tar con el comando `tar -c` y agregamos la opción `-f` para poder asignarle un nombre al archivo. El `./*` indica que todos los archivos y directorios en el directorio actual deben ser incluidos en este proceso. Y por último, calculamos su suma de verificación con el comando `sha256sum` la cual se guarda en el archivo previamente creado 'suma_ver.txt', lanzando un mensaje de finalización y saliendo con éxito.

- [internet.sh](src/scripts/internet.sh): está hecha con el objetivo es verificar la conexión a internet de manera simple, utilizando el comando `ping`.
Primero utilizamos el comando `echo` para así informarle al usuario que se está iniciando el proceso de verificación de la conexión a internet. Después se utiliza el comando `ping` para mandar 5 paquetes con la opción `-q` para que `ping` trabaje sin mostrar mensajes, solo los resultados y la opción `-c 5` para enviar los 5 paquetes.
Una vez que ping termina, verificamos si el comando termino con éxito y, si fue así, el comando retorna "Conexión establecida". Caso contrario, devuelve "Falló la conexión".

- [extra.sh](src/scripts/internet.sh): está diseñada para eliminar archivos y directorios en el directorio actual, excluyendo aquellos con la extensión '.md'.
Se muestra un mensaje en la terminal para informar al usuario que el proceso de eliminación de archivos está por comenzar. pusimos un `sleep 5` que da un tiempo de espera de 5 segundos.
Luego utilizamos un `find` para buscar y eliminar los archivos y directorios en el directorio actual, excluyendo a los que tienen la extensión `.md` usando el `-mindepth 1` que asegura que se busquen solo archivos y directorios que estén al menos a un nivel de profundidad del directorio actual, excluyendo el propio directorio base, o sea el directorio actual `.`.
Con `-exec rm -rf {} +` se ejecuta el comando `rm -rf`, con `-r` para recursividad y `-f` para forzar la eliminación sin preguntas, para cada archivo y directorio encontrado.
Por último mostramos un mensaje confirmando que los archivos fueron eliminados.

#### Integrantes

* Joaquín Aguilera
* Mia Rotili
