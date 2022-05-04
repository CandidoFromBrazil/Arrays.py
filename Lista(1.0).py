"""Repetição do tamanho fixo da lista"""

L = [1, 2, 3]
x = 0
while x < 3:
    print(L[x])
    x += 1

"""Repetição do tamanho fixo da lista <len>"""

L = [1, 2, 3]
x = 0
while x < len(L): #O <len(interável)> da Interável, substitui um dos parâmetros de <while>
    print(L[x])
    x += 1