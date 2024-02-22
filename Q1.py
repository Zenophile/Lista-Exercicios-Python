'''1. Escreva uma função Python para multiplicar todos os números em uma lista.
Exemplo: (8, 2, 3, -1, 7)
Resultado esperado: -336'''



lista = []
p = 0
lista_tamanho = int(input())

for x in range(lista_tamanho):
    z = int(input())
    lista.append(z)

for y in lista:
    p += y
print(lista)

print(p)

#DONE!
