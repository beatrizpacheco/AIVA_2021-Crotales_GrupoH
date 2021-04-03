import unittest
import cv2
import main

class TestCrotalRecogniser(unittest.TestCase):
    def test_RecogniseCrotal(self):
        crotal = cv2.imread("./CrotalesDB/TestSamples/0073.tif")
        recogniser = main
        result = recogniser.prueba(crotal)
        self.assertEqual(result, "6711")
        # El método assertEqual compara que el resultado obtenido y el esperado es el mismo


if __name__ == "__main__":
    unittest.main()  # llama a la clase unittest y ejecuta los test que se tienen definidos
