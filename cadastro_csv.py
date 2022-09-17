# -*- coding: utf-8 -*-

# fazer cadastro no arquivo csv
import csv

header = ['nome', 'sobrenome']
dados = []
opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opt != '0':
    nome = input('Qual o seu nome? ')
    sobrenome = input('Qual o seu sobrenome? ')
    dados.append([nome,sobrenome])
    opt = input(') que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

# escrevendo no arquivo csv
with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)

# lendo um arquivo csv
with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)