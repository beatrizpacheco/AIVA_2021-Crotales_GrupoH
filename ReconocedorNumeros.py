def __get_number_data__(dato):
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


def __get_number_str__(dato):
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

    numbers = __get_number_data__(data_umb)
    if len(numbers) < 4 or len(numbers) > 5:
        numbers = __get_number_data__(data_org)

    if len(numbers) < 4 or len(numbers) > 5:
        numbers = __get_number_str__(string_umb)

    if len(numbers) < 4 or len(numbers) > 5:
        numbers = __get_number_str__(string_org)

    return numbers