'''5. Escreva um programa Python para extrair palavras de vários arquivos de texto (pelos
menos 5 arquivos contendo textos distintos) e colocá-las em uma lista contendo
apenas as palavras distintas.'''

#a variável caminho corresponde ao caminho no MEU computador, você deve alterar o endereço de acordo com o seu PC
import os



lista = []
caminho = "\\Users\\odirc\\OneDrive\\Área de Trabalho\\Nova pasta"

for file in os.listdir(caminho):
    if file.endswith(".txt"):
        with open(os.path.join(caminho, file), 'r') as f:
            conteudo = f.read()
            lista.extend(conteudo.split())





unico = list(set(lista))

for x in unico:
    print(x)

#DONE!
