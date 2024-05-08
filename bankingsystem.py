# Desenvolvimento de um Sistema Bancário

menu = """

    [d] Depositar
    [s] Saque
    [e] Extrato
    [q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_de_saque = 0
LIMITE_DE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        deposito = int(input("Digite o deposito que deseja depositar: "))
        if deposito >= 0:
            saldo += deposito
            print(f"Foi depositado o valor de R${deposito: .2f}")
            opcao = "e"
        else:
            print("Valor inválido")
    elif opcao == "s":
        if numero_de_saque >= LIMITE_DE_SAQUE: 
            print("Você atingiu o limite de saque permitido.")
        else:
            saque = int(input("Digite o valor que deseja sacar: "))
            if saque >= limite:
                print(f"Não é permitido saque com valores acima de R$ {limite: .2f}")
            elif saque >= saldo:
                print("O valor de saque é maior que o valor em saldo.")
            else:
                saldo -= saque
                numero_de_saque += 1
                print(f"Você sacou R${saque: .2f} da conta.")



    elif opcao == "e":
        print(f"A conta tem o valor de R$ {saldo: .2f}")
    elif opcao == "q":
        print("Fim da operação")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")