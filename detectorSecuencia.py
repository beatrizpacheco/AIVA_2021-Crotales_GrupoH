import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_data(d):
    n_boxes =[]
    for i in range(0,len(d['text'])):
        if (d['text'][i] != ""):
            n_boxes.append(d['text'][i])
            #for j in range(0, len(d['text'][i])):
                #if ~d['text'][i][j].isnumeric():
                    #break


    return str(n_boxes)

def detector(img_org, img_umb):
    '''
    ESTAMOS BUSCANDO POR LOS ÚLTIMOS VALORES DEL STRING Y NO POR POSICIONES O TAMAÑOS
    PENDIENTE DE MEJORA
    '''
    # box_org = pytesseract.image_to_boxes(img_org)
    # box_umb = pytesseract.image_to_boxes(img_umb)
    # print("box es: ", box_org)
    # print("box es: ", box_umb)

    string_org = pytesseract.image_to_string(img_org, config='--psm 6')# 6 -c tessedit_char_whitelist=0123456789')
    string_umb = pytesseract.image_to_string(img_umb, config='--psm 6')  # 6 -c tessedit_char_whitelist=0123456789')
    #print("string es: ", string_org)
    #print("string es: ", string_umb)

    data_org = pytesseract.image_to_data(img_org, config='--psm 6', output_type=Output.DICT)
    #print("data es: ", data_org)
    data_org = get_data(data_org)
    data_umb = pytesseract.image_to_data(img_umb, config='--psm 6', output_type=Output.DICT)
    #print("data es: ", data_umb)
    data_umb = get_data(data_umb)

    return string_org, string_umb, data_org, data_umb