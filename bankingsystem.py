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
        deposito = float(input("Digite o deposito que deseja depositar: "))
        if deposito >= 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito: .2f}\n"
        else:
            print("Valor inválido")
    elif opcao == "s":
        if numero_de_saque >= LIMITE_DE_SAQUE: 
            print("Você atingiu o limite de saque permitido.")
        else:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque >= limite:
                print(f"Não é permitido saque com valores acima de R$ {limite: .2f}")
            elif saque >= saldo:
                print("O valor de saque é maior que o valor em saldo.")
            else:
                saldo -= saque
                numero_de_saque += 1
                extrato += f"Saque: R$ {saque: .2f}\n"



    elif opcao == "e":
        print(f"{extrato}")
        print(f"Extrato: R$ {saldo: .2f}")
              
    elif opcao == "q":
        print("Fim da operação")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")