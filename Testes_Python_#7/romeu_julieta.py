"""
Problema:

 Uma entrada de valores numéricos (uma lista deles) 
 
 3x -> Queijo
 5x -> Goiabada
 3x e 5x -> Romeu e Julieta
 
"""

from unittest import TestCase, main
from app import romeu_julieta


class TesteRomeuJulieta(TestCase):
    # def test_existe(self):
    #     romeu_julieta()
        
    def teste_rej_deve_retornar_queijo_3(self):
        """ romeu_julieta(3) -> 'Queijo' """
        valor_entrada = 3
        valor_esperado = 'queijo'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)

    def teste_rej_deve_retornar_goiabada_5(self):
        """ romeu_julieta(5) -> 'Goiabada' """
        valor_entrada = 5
        valor_esperado = 'goiabada'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)

    def teste_rej_deve_retornar_juntos_15(self):
        """ romeu_julieta(15) -> 'Queijo e Goiabada' """
        valor_entrada = 15
        valor_esperado = 'romeu e julieta'
        self.assertEqual(romeu_julieta(valor_entrada), valor_esperado)
        
        
main()