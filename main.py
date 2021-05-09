import cv2
import argparse
import NumCrotalLib

if __name__ == "__main__":
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument("--image_crotal", required=True, help="path to where the images files resides")

    args = vars(ap.parse_args())
    path_image = args['image_crotal']
    '''
    imagen_in = cv2.imread("/usr/src/app/CrotalesDB/TestSamples/0002.TIF")
    #imagen_in = cv2.imread(path_image)
    crotal = NumCrotalLib.reconocedor_crotal(imagen_in)
    print("el numero de crotal es: ", crotal)
