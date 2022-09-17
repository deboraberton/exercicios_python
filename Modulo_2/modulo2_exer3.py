# -*- coding: utf-8 -*-

"""Faça uma função que recebe duas listas e retorna a soma item a item dessas
listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
retornar [1+3, 4+5, 3+1] = [4, 9, 4]"""


def soma_lista():
    lista1 = [1,2,3,4,5]
    lista2 = [1,2,3,4,5]
    lista3 = [num1 + num2 for num1, num2 in zip(lista1, lista2)]
    print(lista3)
    
resultado = soma_lista()