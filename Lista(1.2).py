"""Adição de elementos à lista"""

"""Atribui valor à lista"""
L = []
while True:
    n = int(input('Digite um número, (0 - para sair): '))
    if n == 0:
        break
    L.append(n)
"""Imprime os números lidos <por indice>"""
x = 0 #nesse caso, nosso contador serve como <indice>
while x < len(L):
    print(L[x])
    x += 1

