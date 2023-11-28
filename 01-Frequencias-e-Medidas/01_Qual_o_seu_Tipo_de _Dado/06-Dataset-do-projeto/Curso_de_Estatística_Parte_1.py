#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

import pandas as pd
import csv
import os

diretorio_atual = os.getcwd()
# print(diretorio_atual)

nome_arquivo = 'dados.csv'

# Abra o arquivo CSV em modo de leitura
with open(nome_arquivo, 'r') as arquivo_csv:
    # Crie um objeto leitor CSV
    leitor = csv.reader(arquivo_csv)

    # Itere pelas linhas do arquivo CSV
    for linha in leitor:
        # Acesse os elementos da linha como uma lista
        # Exemplo: linha[0] acessa o primeiro elemento da linha
        print(linha)

dados = pd.read_csv('dados.csv')

print(type(dados))
