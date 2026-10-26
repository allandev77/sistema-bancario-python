
escolha = 0
saldo = 1000.0

while escolha != 4:

    print('''===== BANCO PYTHON =====
[1] Consultar saldo
[2] Depositar
[3] Sacar
[4] Sair
''')

    escolha = int(input("Escolha: "))

    if escolha == 1:
        print('''Seu saldo é de {:.2f} R$
'''.format(saldo))

    elif escolha == 2:
        deposito = float(input("Valor do depósito: "))

        if deposito > 0:
            saldo = saldo + deposito
            print("Depósito realizado com sucesso!")
            print("Seu saldo atual é de {:.2f} R$".format(saldo))

        else:
            print("Depósito não realizado: o valor deve ser positivo.")

    elif escolha == 3:
        saque = float(input("Valor do saque: "))

        if saque > saldo:
            print("Saldo insuficiente!")

        elif saque <= 0:
            print("Saque não realizado: o valor deve ser positivo.")

        else:
            saldo = saldo - saque
            print("Saque realizado com sucesso!")
            print("Saldo atual: {:.2f} R$".format(saldo))

    elif escolha == 4:
        print('''Saindo do sistema.
Volte sempre!''')

    else:
        print("Opção inválida! Tente novamente.")

