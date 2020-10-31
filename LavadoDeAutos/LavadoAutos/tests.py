from django.test import TestCase
import unittest, unicodedata
from .models import Insumos
from django.contrib.auth.models import User

# Create your tests here.
class TestEjemplos(unittest.TestCase):
    def test_iguales_objetos(self):
        self.assertEqual('aa','aa')

    def test_no_hay_texto(self):

        self.assertFalse('Colo Colo' in '   Aguante colo colo')

class TestValidaciones(unittest.TestCase):
    def registrar_insumo(self):
        num = 0
        try:
            insumo = Insumos(
                nombreinsumo = 'Franco',
                precio = 2000,
                descripcion = 'pera',
                stock = 1
            )
            insumo.save()
            num =1
        except:
            num =0
        self.assertEqual(num,1)

    def setUp(self):
        self.test_user = User(email="prueba@prueba.com", name='test user')
        self.test_user.save()

if __name__ == "__main__":
    unittest.main()
    