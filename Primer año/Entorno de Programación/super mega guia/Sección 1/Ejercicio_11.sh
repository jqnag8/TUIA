NOMBRE1=Ariel
NOMBRE2=Ari*
NOMBRE3="Ari *"

echo "Hola *"
echo 'Hola *'
echo 'Hola \*'
echo "Hola \*"
echo "Hola $NOMBRE1"
echo "Hola $NOMBRE2"
echo "Hola \$NOMBRE1"
echo 'Hola $NOMBRE2'
echo "Hola `echo $NOMBRE1`"
echo "Hola `echo $NOMBRE2`"
echo "Hola `echo $NOMBRE3`"

