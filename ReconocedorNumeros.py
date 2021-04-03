
def reconocedor(img, string):
    '''
    DEVOLVEMOS LOS NÚMEROS DE LAS ÚLTIMAS POSICIONES
    PENDIENTE MEJORAR MÉTODO ANTERIOR CON IMAGEN Y SU POSICIÓN
    '''

    numbers = ""

    for i in string[-9:]:
        if i.isnumeric():
            numbers = numbers + i
    #print(numbers)
    return numbers