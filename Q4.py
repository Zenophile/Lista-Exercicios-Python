'''Escreva um programa Python que tome um arquivo de texto (contendo um texto com
pelo menos 6 mil caracteres) como entrada e retorne o número de palavras desse
arquivo. (as palavras contadas podem ser repetidas)'''
nome_arquivo = input()
z = 0

try:
    with open(nome_arquivo, 'r') as x:
        arquivo = x.read()
        palavras = arquivo.split()
        numero_palavras = len(palavras)
        print(f'Esse arquvio tem {numero_palavras} palavras')
except FileNotFoundError:
    print('Esse arquivo não existe')

#DONE!
