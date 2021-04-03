# AIVA_2021-Crotales_GrupoH

Este proyecto consiste en el diseño de una biblioteca para reconocer la secuencia numérica principal situada en los crotales. Esta biblioteca debe ser compatible con Java, y se llamará NumCrotalLib. Será capaz de reconocer los números principales situados en la parte inferior de los crotales mediante las imágenes que le serán proporcionadas. El objetivo será superar una tasa de acierto del 85%.

¿Cómo poner en marcha el proyecto?

Esta versión de la aplicación se ha puesto en funcionamiento con Python 3.8.8. Otras librerías que hemos usado en el desarrollo han sido: OpenCV(4.5.1), pandas(1.2.3), unittest, pytesseract (0.3.7).

Descargar la librería pytesseract de la web "https://github.com/UB-Mannheim/tesseract/wiki". En la línea 3 del programa detectorSecuenciaPrincipal, se debe cambiar la ruta de instalación de pytesseract: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'.

Para descargarse el programa, se necesita realizar "clone https://github.com/beatrizpacheco/AIVA_2021-Crotales_GrupoH.git". 

Si se quiere ejecutar una prueba individual, ejecutar main.py, y en la línea 21 poner la ruta de la imagen a probar. Si se quieren ejecutar las pruebas estadísticas, ejecutar EstadisticasReconocimiento.py. Si se quiere ejecutar un test unitario individual, ejecutar CrotalTest.py cambiando la línea 7 con la ruta de la imagen a probar.
