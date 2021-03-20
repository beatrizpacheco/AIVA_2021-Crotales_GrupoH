import pandas as pd
import cv2
from Crotalrecogniser import Crotalrecogniser


class MakeTests():
    def __init__(self):
        self.recogniser = Crotalrecogniser()
        self.sucess = 0
        self.test = 0
        csv_reader = pd.read_excel('./GroundTruth.ods',  header=0, converters={'NUM_DOCUMENTO': str, 'Real': str})
        for row in csv_reader.values:
            file_name = row[0]
            file_name = file_name[-5:]
            file_name = str(int(file_name) + 10001)
            file_name = file_name[-4:]
            file_name = file_name + ".TIF"
            groundtruth = row[1]
            self._procesar(file_name, groundtruth)
        print("la tasa de acierto es de ", self.sucess/self.test)

    def _procesar(self, file_name, groundtruth):
        img = cv2.imread(file_name)
        result = self.recogniser.recognise(img)
        self.test += 1
        if result == groundtruth:
            self.sucess +=1


if __name__ == "__main__":
    m = MakeTests()