# -*- coding: utf-8 -*-

"""Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
programa deve imprimir a mensagem “O novo valor é [valor]”"""

porcentagem = 15
valor = float(input('Informe o valor monetário:'))
print('Valor atual:',valor)

porcentagem = (valor * porcentagem) / 100
valor = valor - porcentagem
print('O novo valor menos 15% é: ', valor)