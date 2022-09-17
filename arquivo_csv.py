# -*- coding: utf-8 -*-

# Manipulação de arquivos csv

import csv  # importar a biblioteca csv

# abrir um arquivo csv
with open('E:/Documentos/covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)


# abrindo apenas linhas expecificas
with open('E:/Documentos/covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next() # essa função pula uma das interações
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)


# criar um arquivo csv
with open('E:/Documentos/users.csv', 'w', encoding='utf-8') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome'])
    escritor.writerows(['Antonio', 'Silva'])

# newline=''  = nao deixar quebra de linha
# with open('E:/Documentos/users.csv', 'w', encoding='utf-8', newline='')

