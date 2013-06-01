#!/usr/bin/env python
# coding: utf-8

import random
import time


def vizinhos(matriz, linha, coluna):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = []
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if (i == linha and j == coluna) or i < 0 or j < 0 or \
                    i > linhas - 1 or j > colunas - 1:
                continue
            resultado.append(matriz[i][j])
    return resultado


def troca_de_estado(matriz):
    nova_matriz = [list(linha) for linha in matriz]
    for num1, linha in enumerate(matriz):
        for num2, elemento in enumerate(linha):
            lista_de_vizinhos = vizinhos(matriz, num1, num2)
            n_vizinhos_vivos = lista_de_vizinhos.count('1')
            if n_vizinhos_vivos < 2 or n_vizinhos_vivos > 3:
                nova_matriz[num1][num2] = '0'
            elif elemento == '0' and n_vizinhos_vivos == 3:
                nova_matriz[num1][num2] = '1'
    return [''.join(linha) for linha in nova_matriz]


def aleatorio():
    return str(random.randint(0, 1))

if __name__ == '__main__':
    n, m = 50, 120
    matriz = [''.join([aleatorio() for i in range(m)]) for j in range(n)]
    quadrado = u'\u25a0'
    while True:
        try:
            print chr(27) + "[2J"
            print '\n'.join(matriz).replace('0', ' ').replace('1', quadrado)
            matriz = troca_de_estado(matriz)
            time.sleep(0.05)
        except KeyboardInterrupt:
            break
