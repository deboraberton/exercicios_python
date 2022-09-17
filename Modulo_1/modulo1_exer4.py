# -*- coding: utf-8 -*-

"""Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops"""

tabuada = int(input('Informe o numero da tabuada: '))
num = 0

while num <= 10:
    valor = tabuada * num
    print(tabuada,' x ',num, '=', valor)
    num = num + 1