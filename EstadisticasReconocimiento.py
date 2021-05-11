import pandas as pd
import cv2
import main

class MakeTests():
    def __init__(self):
        self.recogniser = main
        self.tp = 0 # acierto
        self.fn = 0 # no detecto números
        self.fp = 0 # detecto números incorrectos
        self.test = 0 # imágenes totales

        #self.images_succes = []
        csv_reader = pd.read_excel('./CrotalesDB/GroundTruth.ods',  header=0, converters={'NUM_DOCUMENTO': str, 'Real': str})
        for row in csv_reader.values:
            file_name = row[0]
            file_name = file_name[-5:]
            file_name = str(int(file_name) + 10001)
            file_name = file_name[-4:]
            file_name = file_name + ".TIF"
            groundtruth = row[1]
            self._procesar(file_name, groundtruth)
        print("la tasa de acierto es de ", self.tp/self.test)
        precision = round(self.tp / (self.tp + self.fp), 3)
        print("precision es: ", precision)
        recall = round(self.tp / (self.tp + self.fn), 3)
        print("recall es: ", recall)
        iou = round(self.tp / (self.fn + self.tp + self.fp),3)
        print("IoU es: ", iou)
        f1 = round((2 * precision * recall) / (precision + recall), 3)
        print("f1 es: ", f1)
        #print("las imagenes acertadas son: ", self.images_succes)

    def _procesar(self, file_name, groundtruth):
        print("./CrotalesDB/TestSamples/" + file_name)
        img = cv2.imread("./CrotalesDB/TestSamples/" + file_name)
        result = self.recogniser.NumCrotalLib.reconocedor_crotal(img)
        self.test += 1
        if result == groundtruth:
            self.tp +=1
            #self.images_succes.append(file_name)
        elif result == "":
            self.fn += 1
        elif result != groundtruth:
            self.fp += 1


if __name__ == "__main__":
    m = MakeTests()