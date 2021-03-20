class Crotalrecogniser:

    def recognise(self, image_crotal):
        """

        :param image_crotal: numpy matrix (n,m)
        #En esta función llamaríamos a Preprocesador, que umbraliza y endereza la imagen en caso necesario, y la devuelve
        #Esa imagen mejorada la pasamos a DetectorSecuenciaPrincipal, que nos devuelve la posición
        #Esa posición, junto a la imagen, la pasamos al ReconocedorNumeros, que devuelve el string final
        :return: texto reconocido en el número principal del crotal en forma de string
        """
        return "0288"
