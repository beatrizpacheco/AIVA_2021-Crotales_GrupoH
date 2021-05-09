# AIVA_2021-Crotales_GrupoH

Este proyecto consiste en el diseño de una biblioteca para reconocer la secuencia numérica principal situada en los crotales. Esta biblioteca debe ser compatible con Java, y se llamará NumCrotalLib. Será capaz de reconocer los números principales situados en la parte inferior de los crotales mediante las imágenes que le serán proporcionadas. El objetivo será superar una tasa de acierto del 85%.

# Cómo poner en marcha el proyecto en local 

Esta versión de la aplicación se ha puesto en funcionamiento con Python 3.8.8. Otras librerías que hemos usado en el desarrollo han sido: OpenCV(4.5.1), pandas(1.2.3), unittest, pytesseract (0.3.7).

Descargar la librería pytesseract de la web "https://github.com/UB-Mannheim/tesseract/wiki". En la línea 3 del programa detectorSecuenciaPrincipal, se debe cambiar la ruta de instalación de pytesseract: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'.

Para descargarse el programa, se necesita realizar "clone https://github.com/beatrizpacheco/AIVA_2021-Crotales_GrupoH.git". 

Si se quiere ejecutar una prueba individual, ejecutar main.py, y en la línea 21 poner la ruta de la imagen a probar. Si se quieren ejecutar las pruebas estadísticas, ejecutar EstadisticasReconocimiento.py. Si se quiere ejecutar un test unitario individual, ejecutar CrotalTest.py cambiando la línea 7 con la ruta de la imagen a probar.

# Despliegue y puesta en marcha sobre Docker

Para poder hacer uso de nuestra biblioteca, nos dirigimos a la web de Docker Hub (https://hub.docker.com/r/grupoh/crotales_java_grupoh), desde donde nos descargaremos la imagen. Copiamos el comando que aparece, y nos dirigimos al terminal de nuestro ordenador (cdm). Introducimos el comando copiado para descargar la imagen (tardará unos segundos):

    docker pull grupoh/crotales_java_grupoh

Para comprobar que se ha descargado correctamente podemos usar el siguiente comando para ver las imágenes disponibles en tu ordenador, en Docker:

    docker images
    
Debe aparecer algo similar a las siguientes líneas, donde podemos ver descargado “grupoh/crotales_java_grupoh”, que ocupa 1.5GB:

    REPOSITORY TAG IMAGE ID CREATED SIZE
    grupoh/crotales_java_grupoh latest 35d3aec68b27 46 minutes ago 1.52GB

A continuación, creamos el contenedor de docker a partir de la imagen que nos acabamos de descargar, con el nombre que queramos (nombre_contenedor):

    docker create -it --name nombre_contenedor grupoh/crotales_java_grupoh bash

Ahora podemos comprobar que se ha creado bien el contenedor, y el estado que tiene con el siguiente comando:

    docker container ls -a

Debe aparecer algo similar a las siguientes líneas, donde podemos ver que se ha creado correctamente el contenedor, y su estado, ahora mismo en “Created”:

    CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
    280734f33a85 grupoh/crotales_java_grupoh "bash" 33 seconds ago Created crotales_cont

Una vez creado el contenedor, tenemos que inicializarlo y conectar nuestro terminal con la aplicación con los siguientes comandos:

    docker start crotales_cont
    docker attach crotales_cont

Nos aparecerá un terminal parecido al siguiente “root@280734f33a85:/usr/src/app#:” donde debemos ejecutar la aplicación con el comando “java Main.java”. Un ejemplo de su funcionamiento es el siguiente:

    root@280734f33a85:/usr/src/app# java Main.java
    el numero de crotal es: 9926
    root@280734f33a85:/usr/src/app#

Ahora mismo está puesta una imagen por defecto (./Crotales/TestSamples/0002.TIF). Para probar la biblioteca con otra imagen debemos hacer uso del editor vim. 

    root@280734f33a85:/usr/src/app# vim main.py
 
Nos aparecerá el archivo en modo lectura. Para cambiar al modo edición tenemos que pulsar la letra “i” (modo insert). Ahora nos moveremos con el cursor hasta la zona señalada en la imagen, e introduciremos el número de imagen que se quiere probar. Una vez modificado, pulsar la tecla “esc” (escape), escribir “:wq” y pulsar Enter, que guardará y cerrará el archivo, volviendo a aparecer el terminal. Ahora podemos ejecutar de nuevo la librería con el comando mencionado anteriormente de “java Main.java”.

Cada vez que se quiera probar otra imagen, se debe de realizar este proceso con el editor vim. 

Para salir del contenedor de docker, basta con escribir “exit” y te devolverá al terminal de tu ordenador. 
    
    root@280734f33a85:/usr/src/app# exit
