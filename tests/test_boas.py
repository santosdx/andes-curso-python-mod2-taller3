import unittest
from models.boaConstrictor import BoaConstrictor


class TestBoaConstrictor(unittest.TestCase):

    def test_hacer_sonido(self):
        boa1 = BoaConstrictor("Chocolate", 8.5, 6, "Brasil", 10)
        self.assertEqual(boa1.hacer_sonido(), "¡Tsss!")

    def test_hacer_sonidocalcular_flete(self):
        boa1 = BoaConstrictor("Chocolate", 8.5, 6, "Brasil", 10)
        self.assertEqual(boa1.calcular_flete(), 85)

    def test_comer(self):
        numero_ratones = 2
        boa1 = BoaConstrictor("Chocolate", 8.5, 6, "Brasil", 10)
        boa1.comer(2)
        #print("La boa comio {0} ratones.".format(boa1.get_kilos_comidos()))
        self.assertEqual(boa1.get_kilos_comidos(), numero_ratones)
