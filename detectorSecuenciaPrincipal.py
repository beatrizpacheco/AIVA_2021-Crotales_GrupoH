import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detector(img):
    '''
    ESTAMOS BUSCANDO POR LOS ÚLTIMOS VALORES DEL STRING Y NO POR POSICIONES O TAMAÑOS
    PENDIENTE DE MEJORA
    '''
    #box = pytesseract.image_to_boxes(img)
    #print("box es: ", box)
    string = pytesseract.image_to_string(img)
    #print("string es: ", string)
    #data = pytesseract.image_to_data(img)
    #print("data es: ", data)
    return string