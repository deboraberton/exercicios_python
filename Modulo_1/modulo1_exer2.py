# -*- coding: utf-8 -*-

"""Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação
inválida"""

idade = int(input('Informe a sua idade:'))
if idade < 150 and idade > 0:
    print('Idade:',idade)
else:
    print('Informação inválida')

salario = float(input('Informe o seu salário:'))
if salario > 0:
    print('Salário:',salario)
else:
    print('Informação inválida')

sexo = input('Informe o sexo, opção: M - Masculino, F - Feminino, O - outros: ')
if sexo == 'F' or sexo == 'f':
    print('Sexo Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Sexo Masculino')
elif sexo == 'O' or sexo == 'o':
    print('Outros sexo')
else:
    print('Informação inválida')
