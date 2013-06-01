# coding: utf-8

import unittest

from gameoflife import vizinhos, troca_de_estado


class TestGameOfLife(unittest.TestCase):
    def test_passando_matriz_retorna_vizinhos(self):
        matriz = '''
        abcd
        efgh
        ijkl
        mnop
        '''.strip().split()

        resultado = vizinhos(matriz, 1, 1)
        esperado = list('abcegijk')
        self.assertEqual(resultado, esperado)

        resultado = vizinhos(matriz, 2, 0)
        esperado = list('efjmn')
        self.assertEqual(resultado, esperado)

        resultado = vizinhos(matriz, 0, 0)
        esperado = list('bef')
        self.assertEqual(resultado, esperado)

        resultado = vizinhos(matriz, 0, 3)
        esperado = list('cgh')
        self.assertEqual(resultado, esperado)

        resultado = vizinhos(matriz, 3, 0)
        esperado = list('ijn')
        self.assertEqual(resultado, esperado)

        resultado = vizinhos(matriz, 3, 3)
        esperado = list('klo')
        self.assertEqual(resultado, esperado)

    def test_troca_de_estado(self):
        matriz = '''
        0101
        0100
        1010
        0011
        '''.strip().split()

        matriz_resultado = troca_de_estado(matriz)

        matriz_esperada = '''
        0010
        1100
        0011
        0111
        '''.strip().split()

        self.assertEqual(matriz_resultado, matriz_esperada)
