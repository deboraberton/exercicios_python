# -*- coding: utf-8 -*-

# ler arquivos txt

arquivo = open('E:/Documentos/dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close() # sempre abrir e fechar o arquivo


#abrindo arquivo com while. passar por todas as linhas com while
arquivo = open('E:/Documentos/dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
linha = arquivo.readline()  #ler a linha do arquivo
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

#abrindo arquivo com for. passar por todas as linhas com for
arquivo = open('E:/Documentos/dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close() 


# abrir arquivo com with sem precisar fechar no final
with open('E:/Documentos/dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)



# 'r' = read = ler um arquivo
# 'w' = write = escrever um arquivo
# 'a' = adicionar texto no arquivo existente

# escrevendo um arquivo com with
with open('E:/Documentos/dom_casmurro_cap_1.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever meu primeiro arquivo')

# abrindo o arquivo criado
with open('E:/Documentos/dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')