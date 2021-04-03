import cv2

def preprocesador(img):
    '''
    FALTA ENDEREZAR Y MEJORAR UMBRALIZADO
    '''
    # Umbralizado
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,umbralizada = cv2.threshold(blur,65,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #_,umbralizada = cv2.threshold(gray, 65, 255, cv2.THRESH_BINARY)
    #umbralizada = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 105, 12)
    #cv2.imshow("umbralizada", umbralizada)
    #cv2.waitKey(0)

    '''
    contours,_ = cv2.findContours(umbralizada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        cv2.drawContours(img,[c],0, (0,255,0), 2)
    umbralizada = cv2.cvtColor(umbralizada, cv2.COLOR_GRAY2BGR)
    img = cv2.polylines(umbralizada, contours, 1, (255, 255, 255))
    cv2.imshow("bordes",img)
    cv2.waitKey(0)
    '''

    return umbralizada

