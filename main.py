import cv2
import Preprocesador
import detectorSecuenciaPrincipal
import ReconocedorNumeros


def prueba(imagen_in):

    #preprocesador
    imagen_prep = Preprocesador.preprocesador(imagen_in)

    #detector
    pos = detectorSecuenciaPrincipal.detector(imagen_prep)

    #reconocedor
    numbers = ReconocedorNumeros.reconocedor(imagen_prep, pos)
    return numbers

if __name__ == "__main__":
    # llamamos imread()
    imagen_in = cv2.imread("./CrotalesDB/TestSamples/0073.TIF")
    prueba(imagen_in)
