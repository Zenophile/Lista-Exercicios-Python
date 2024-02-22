'''Escreva uma função Python que pegue uma lista e retorne uma nova lista com
elementos distintos da primeira lista.
Exemplo: [1,2,3,3,3,3,4,5]
Resultado esperado: [1, 2, 3, 4, 5]'''



lista = []

lista_tamanho = int(input())

for x in range(lista_tamanho):
    z = int(input())
    lista.append(z)

lista_distinta = set(lista)

print(lista_distinta)

#DONE!
