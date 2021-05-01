import cv2
import Preprocesador
import detectorSecuencia
import ReconocedorNumeros
import os


def prueba(imagen_in): #, filename):

    #preprocesador
    imagen_prep_org, imagen_prep_umb = Preprocesador.preprocesador(imagen_in)
    '''
    path = "resultado"
    if not os.path.isdir(path):
        os.mkdir(path)
    filename = path + "/" + filename
    cv2.imwrite(filename, imagen_prep_umb)
    '''
    #detector
    string_org, string_umb, data_org, data_umb = detectorSecuencia.detector(imagen_prep_org, imagen_prep_umb)

    #reconocedor
    numbers = ReconocedorNumeros.reconocedor(string_org, string_umb, data_org, data_umb)
    return numbers

if __name__ == "__main__":
    # llamamos imread()
    imagen_in = cv2.imread("./CrotalesDB/TestSamples/0073.TIF")
    crotal = prueba(imagen_in)
    print("el numero de crotal es: ", crotal)
