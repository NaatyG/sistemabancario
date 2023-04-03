depositos = []
saques = []
saldo = 0
saques_diarios = 0

while True:
    print("========= MENU =========")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            depositos.append(valor_deposito)
            saldo += valor_deposito
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")

    elif opcao == 2:
        if saques_diarios < 3:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 0 and valor_saque <= 500 and valor_saque <= saldo:
                saques.append(valor_saque)
                saldo -= valor_saque
                saques_diarios += 1
                print("Saque realizado com sucesso.")
            elif valor_saque > 500:
                print("Valor inválido. O limite de saque é de R$500 por operação.")
            elif valor_saque > saldo:
                print("Saldo insuficiente.")
            else:
                print("Valor inválido. O saque deve ser maior que zero.")
        else:
            print("Número máximo de saques diários atingido.")

    elif opcao == 3:
        print("========= EXTRATO =========")
        print("DEPÓSITOS:")
        for deposito in depositos:
            print("R$ {:.2f}".format(deposito))
        print("SAQUES:")
        for saque in saques:
            print("R$ {:.2f}".format(saque))
        print("SALDO: R$ {:.2f}".format(saldo))

    elif opcao == 4:
        print("Saindo do sistema bancário...")
        break

    else:
        print("Opção inválida.")
