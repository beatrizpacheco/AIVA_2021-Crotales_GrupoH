import pandas as pd
import cv2
import main

class MakeTests():
    def __init__(self):
        self.recogniser = main
        self.sucess = 0
        self.test = 0
        self.images_succes = []
        csv_reader = pd.read_excel('./CrotalesDB/GroundTruth.ods',  header=0, converters={'NUM_DOCUMENTO': str, 'Real': str})
        for row in csv_reader.values:
            file_name = row[0]
            file_name = file_name[-5:]
            file_name = str(int(file_name) + 10001)
            file_name = file_name[-4:]
            file_name = file_name + ".TIF"
            groundtruth = row[1]
            self._procesar(file_name, groundtruth)
        print("la tasa de acierto es de ", self.sucess/self.test)
        print("las imagenes acertadas son: ", self.images_succes)

    def _procesar(self, file_name, groundtruth):
        print("./CrotalesDB/TestSamples/" + file_name)
        img = cv2.imread("./CrotalesDB/TestSamples/" + file_name)
        result = self.recogniser.prueba(img)
        self.test += 1
        if result == groundtruth:
            self.sucess +=1
            self.images_succes.append(file_name)

if __name__ == "__main__":
    m = MakeTests()