# -*- coding: utf-8 -*-

"""Faça um programa que olhe todos os itens de uma lista e diga quantos deles
são pares"""

lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista2 = []

for valor in lista1:
    if valor % 2 == 0:
        lista2.append(valor)

print(lista2)