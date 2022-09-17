# -*- coding: utf-8 -*-

"""Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados"""

print('Responda as perguntas com SIM ou NAO')
lista = ['SIM','NAO']
contagem = 0

p1 = input('Mora perto da vítima? ')
if p1 not in lista:
    p1 = input('Resposta inválida, Mora perto da vítima? ')
if p1 == 'SIM':
    contagem = contagem + 1

p2 = input('Já trabalhou com a vítima? ')
if p2 not in lista:
    p2 = input('Resposta inválida, Já trabalhou com a vítima? ')
if p2 == 'SIM':
    contagem = contagem + 1
        

p3 = input('Telefonou para a vítima? ')
if p3 not in lista:
    p3 = input('Resposta inválida, Telefonou para a vítima? ')
if p3 == 'SIM':
    contagem = contagem + 1
        

p4 = input('Esteve no local do crime? ')
if p4 not in lista:
    p4 = input('Resposta inválida, Esteve no local do crime? ')
if p4 == 'SIM':
    contagem = contagem + 1
        

p5 = input('Devia para a vítima? ')
if p5 not in lista:
    p5 = input('Resposta inválida, Devia para a vítima? ')
if p5 == 'SIM':
    contagem = contagem + 1
        

if contagem <= 1:
    print('Está Liberado')
elif contagem == 2:
    print('É Suspeito')
elif contagem == 3 or contagem == 4:
    print(' Cúmplice do crime')
elif contagem == 5:
    print('É o Assassino')
