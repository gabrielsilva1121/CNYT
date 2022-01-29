import unittest
from Libreria_cuantica_1 import *
class TestStringMethods (unittest.TestCase):
    def test_suma(self):
        a = (1,4)
        b = (5,2)
        self.assertEqual(sumaComplejos(a,b),(6,6))
    def test_resta(self):
        a = (1,4)
        b = (5,2)
        self.assertEqual(restaComplejos(a,b),(-4,2))
    def test_multiplicacion(self):
        a = (1,4)
        b = (5,2)
        self.assertEqual(multiComplejos(a,b),(-3,22))
    def test_division(self):
        a = (1,4)
        b = (5,2)
        self.assertEqual(divcomplejos(a,b),(0.4482758620689655,0.10344827586206896))
    def test_conjugado(self):
        a = (1,4)
        self.assertEqual(conjugadoComplejo(a),(1,-4))
    def test_modulo(self):
        a = (1,4)
        self.assertEqual(moduloComplejo(a),(8.5))
    def test_carteapolar(self):
        a = (1,4)
        self.assertEqual(carteAPolar(a),(8.5, 1.3258176636680326))
    def test_fase(self):
        a = (1,4)
        self.assertEqual(fase(a),(1.3258176636680326))
        
        
if __name__ == '__main__':
    unittest.main()
