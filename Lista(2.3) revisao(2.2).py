"""Programa - Simulação de uma fila de banco"""

ultimo = 10
fila = list(range(1, ultimo + 1)) #por ser lis(n-), mas acrecentado +1, o cliente passa a contar de 1 - 10, e não de 1 - 9
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite (F) para adicionar um cliente ao fim da fila")
    print("ou (A) para realizar o atendimento. (S) para sair: ")
    operacao = str(input("Operação (F,A ou S): "))
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0) # o responsável por subttrair o valor da lista <fila no caso boy>
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vázia! ninguém para atender.")
    elif operacao == "F":
        ultimo += 1 #incrementa o ticket do novo cliente
        fila.append(ultimo) #Adição do ticket do cliente na lista
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S")