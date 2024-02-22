'''6. Tomando a lista de palavras encontrada no exercício anterior, escreva um programa
Python para gerar 26 arquivos de texto chamados A.txt, B.txt e assim por diante até
Z.txt. Em cada arquivo escrever as palavras que iniciam pelo caractere especificado no
nome do arquivo.'''

import os
import string



os.listdir()

caminho = "\\Users\\odirc\\OneDrive\\Área de Trabalho\\Nova pasta"
caminho2 = "\\Users\\odirc\\PycharmProjects\\Lista3"
for char in string.ascii_lowercase:
    with open(os.path.join(caminho2, char), 'w') as f:
        f.write(char)


for file in os.listdir(caminho2):
    if file[0].islower():
        with open(os.path.join(caminho2, file), 'w') as x:
            x.write(file[0])






'''Não consigo testar o programa, pois ele gera o seguinte erro
PermissionError: [Errno 13] Permission denied: '\\Users\\odirc\\PycharmProjects\\Lista3\\venv'
Já tentei de tudo e não sei o que fazer, mas ele ainda não está completo'''
