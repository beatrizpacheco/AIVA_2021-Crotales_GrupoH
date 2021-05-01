import cv2
import re
import pytesseract
from pytesseract import Output
import numpy as np
from skimage.morphology import skeletonize


def enderezar(image_umbralizada, image_org):
    coords = np.column_stack(np.where(image_umbralizada > 0))
    #print((coords)[-1])
    angle = cv2.minAreaRect(coords)[-1]
    if angle < 90 and angle > 45:
        angle = (90 - angle)
    elif angle < 45 and angle > 0:
        angle = (360 - angle)
    elif angle == 90:
        angle = 0
    elif angle > 90 and angle < 180:
        angle = 180 - angle + 270
    else:
        angle = -angle
    (h, w) = image_umbralizada.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_org = cv2.warpAffine(image_org, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    rotated_umb = cv2.warpAffine(image_umbralizada, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated_org, rotated_umb

def recortar(umbralizada, img):
    (x, y) = np.where(umbralizada == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    recorte_umb = umbralizada[topx:bottomx + 1, topy:bottomy + 1]
    recorte_org = img[topx:bottomx + 1, topy:bottomy + 1]

    return recorte_org, recorte_umb

def preprocesador(img):
    '''
    FALTA ENDEREZAR Y MEJORAR UMBRALIZADO
    '''
    # Umbralizado

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(15,15),0)

    _, umbralizada = cv2.threshold(blur, 113, 255, cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    apertura = cv2.morphologyEx(umbralizada, cv2.MORPH_OPEN, kernel)

    #umbralizada = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.ADAPTIVE_THRESH_MEAN_C, 11, 2)


    recorte_org, recorte_umb = recortar(apertura, img)

    corregida_org, corregida_umb = enderezar(recorte_umb, recorte_org)

    '''
    box = pytesseract.image_to_boxes(corregida)
    print("box es: ", box)
    d = pytesseract.image_to_data(corregida)
    print(d)
    d = pytesseract.image_to_data(corregida, output_type=Output.DICT)
    print(d.keys())
    '''
    '''
    img_draw = recorte_umbralizada.copy()
    d = pytesseract.image_to_data(corregida, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img_draw = cv2.rectangle(corregida, (x, y), (x + w, y + h), (0, 255, 0), 2)
    '''
    '''
    max_c = []
    max = 0
    contours,hierarchy  = cv2.findContours(umbralizada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        cv2.waitKey(0)
        if area > max:
            max = area
            max_c = c

    cv2.drawContours(img,[max_c],0, (0,255,0), 2)
    for i in range(0, len(max_c)):

    #cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    #umbralizada = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    #img = cv2.polylines(umbralizada, contours, 1, (255, 255, 255))
    cv2.imshow("bordes",img)
    cv2.waitKey(0)
    '''


    return corregida_org, corregida_umb


