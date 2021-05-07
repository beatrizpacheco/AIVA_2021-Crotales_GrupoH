import cv2
import numpy as np

def __enderezar__(image_umbralizada, image_org):
    coords = np.column_stack(np.where(image_umbralizada > 0))
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

def __recortar__(umbralizada, img):
    (x, y) = np.where(umbralizada == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    recorte_umb = umbralizada[topx:bottomx + 1, topy:bottomy + 1]
    recorte_org = img[topx:bottomx + 1, topy:bottomy + 1]

    return recorte_org, recorte_umb

def preprocesador(img):
    # Umbralizado
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(15,15),0)

    _, umbralizada = cv2.threshold(blur, 113, 255, cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    apertura = cv2.morphologyEx(umbralizada, cv2.MORPH_OPEN, kernel)

    recorte_org, recorte_umb = __recortar__(apertura, img)

    corregida_org, corregida_umb = __enderezar__(recorte_umb, recorte_org)

    return corregida_org, corregida_umb


