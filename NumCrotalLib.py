import Preprocesador
import detectorSecuencia
import ReconocedorNumeros


def reconocedor_crotal(imagen_in):
    #preprocesador
    imagen_prep_org, imagen_prep_umb = Preprocesador.preprocesador(imagen_in)

    #detector
    string_org, string_umb, data_org, data_umb = detectorSecuencia.detector(imagen_prep_org, imagen_prep_umb)

    #reconocedor
    numbers = ReconocedorNumeros.reconocedor(string_org, string_umb, data_org, data_umb)
    return numbers