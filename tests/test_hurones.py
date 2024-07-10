import unittest
from models.huron import Huron


class TestHuron(unittest.TestCase):

    def test_hacer_sonido(self):
        huron1 = Huron("Kled", 4, 2, "Australia", 5)
        self.assertEqual(huron1.hacer_sonido(), "¡Eek Eek!")

    def test_hacer_sonidocalcular_flete(self):
        huron1 = Huron("Kled", 4, 2, "Australia", 5)
        self.assertEqual(huron1.calcular_flete(), 20)
