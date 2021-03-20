import unittest
import cv2
from Crotalrecogniser import Crotalrecogniser

class TestCrotalRecogniser(unittest.TestCase):
    def test_RecogniseCrotal(self):
        crotal = cv2.imread("0000.tif")
        recogniser = Crotalrecogniser()
        result = recogniser.recognise(crotal)
        self.assertEqual(result, "0288")  # El método assertEqual compara que el resultado obtenido y el esperado es el mismo


if __name__ == "__main__":
    unittest.main()  # llama a la clase unittest y ejecuta los test que se tienen definidos
