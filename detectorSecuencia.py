import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def __get_data__(d):
    n_boxes =[]
    for i in range(0,len(d['text'])):
        if (d['text'][i] != ""):
            n_boxes.append(d['text'][i])


    return str(n_boxes)

def detector(img_org, img_umb):

    string_org = pytesseract.image_to_string(img_org, config='--psm 6')
    string_umb = pytesseract.image_to_string(img_umb, config='--psm 6')
    #print("string es: ", string_org)
    #print("string es: ", string_umb)

    data_org = pytesseract.image_to_data(img_org, config='--psm 6', output_type=Output.DICT)
    #print("data es: ", data_org)
    data_org = __get_data__(data_org)
    data_umb = pytesseract.image_to_data(img_umb, config='--psm 6', output_type=Output.DICT)
    #print("data es: ", data_umb)
    data_umb = __get_data__(data_umb)

    return string_org, string_umb, data_org, data_umb