import unittest
from cripto import posicao, recupera, rot13

class TestRot13(unittest.TestCase):
    def test_rot13_string_simples(self):
        entrada = "HELLO"
        saida = "URYYB"
        resultado = rot13(entrada)
        self.assertEqual(saida, resultado)

    def test_recupera_caractere(self):
        entrada = 3
        saida = "D"
        resultado = recupera(entrada)
        self.assertEqual(saida, resultado)


if __name__== '__main__':
    unittest.main()      