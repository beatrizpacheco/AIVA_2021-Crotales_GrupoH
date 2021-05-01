def get_number_data(dato):
    contador = 0
    numbers = ""
    for _, j in enumerate(dato[::-1]):
        if j.isnumeric():
            numbers = numbers + j
            contador += 1
            if contador == 4:
                break
    numbers = numbers[::-1]
    return numbers


def get_number_str(dato):
    contador = 0
    numbers = ""
    for i in reversed(dato):
        if i.isnumeric():
            numbers = numbers + i
            contador += 1
            if contador == 4:
                break
    numbers = numbers[::-1]

    return numbers



def reconocedor(string_org, string_umb, data_org, data_umb):
    '''
    DEVOLVEMOS LOS NÚMEROS DE LAS ÚLTIMAS POSICIONES
    PENDIENTE MEJORAR MÉTODO ANTERIOR CON IMAGEN Y SU POSICIÓN
    '''

    numbers = get_number_data(data_umb)
    if len(numbers) < 4 or len(numbers) > 5:
        numbers = get_number_data(data_org)

    if len(numbers) < 4 or len(numbers) > 5:
        numbers = get_number_str(string_umb)

    if len(numbers) < 4 or len(numbers) > 5:
        numbers = get_number_str(string_org)

    #print("el numero de crotal es: ", numbers)


    return numbers