"""Pesquisa Sequencial - mas sem a váriavél <achou<Bool>> usando dois input"""
L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
achado1 = False
achado2 = False
x = 0
while x < len(L):
    if L[x] == p:
        achado1 = True
        break
    if L[x] == v:
        achado2 = True
        break
    x += 1
if achado1:
    print(f'Primeiro valor digitado: {p}, achado na posição: {x} da lista {L}')
elif achado2:
    print(f'Segundo valor digitado: {v} , achado na posição: {x} da lista {L}')
else:
    print('Nenhum valor achado')