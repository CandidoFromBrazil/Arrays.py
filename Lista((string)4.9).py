"""Criação e impressão da lista compras"""

compras = []
while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: '))
    compras.append([produto, quantidade, preco])
    soma = 0.0
    for e in compras:
        print(f'\n{e[0]:5s},{e[1]:3d} X {e[2]:5.2f} ={e[1] * e[2]:6.2f}')
        soma += e[1] * e[2]
    print(f'Total: {soma:7.2f}\n')