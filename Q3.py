''' 3 Dicionários são estruturas de dados bastante versáteis. O fato de podermos
adicionarmos pares de chaves únicas e seus respectivos valores podendo estes serem
de tipos variáveis, porém, faz com que o conceito de ordenação não seja aplicável
nessa estrutura (por exemplo, um dicionário com 2 itens pode conter uma chave com
valor [1,"abc", "Brasil", 17.92] e outra com valor 10. Como comparar esses valores de
forma a ordená-los?). Porém, em certos casos, existe a possibilidade de ordenação
quando as chaves são compostas por valores de mesmos tipos ou tipos comparáveis
(exemplo, chaves do tipo string). Crie um dicionário com chaves do tipo string
contendo o nome de pessoas e para cada item (pessoa) a perspectiva idade dessa
pessoa. Execute um laço mostrando a idade das pessoas por ordem alfabética.'''


dicio = {"Odir": "23",
         "Gustavo": "25",
         "Abner": "15",
         "Bobão": "30",
         "Cascão": "50,"}

dicio_alfa = sorted(dicio.items())

print(dicio_alfa)


#DONE!

