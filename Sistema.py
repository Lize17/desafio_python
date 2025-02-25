
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo_conta = 0 
limite = 500
extrato = ""
n_saques = 0
limite_saques = 3


while True:
    opcao = input(menu)

    if opcao == '1':

        valor_deposito = float(input("Informe o valor do deposito: "))

        if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato +=f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Operação falhou!. O valor informado é invalido")
    
    elif opcao == '2':
        valor_saque = float(input("Informe o valor do saque: "))

        if valor_saque > saldo_conta:
            print("Operação falhou!. Saldo insuficiente")
        
        elif valor_saque > limite:
            print("Operação falhou!. O valor do saque ultrapassa o limite")
        
        elif n_saques >= limite_saques:
            print("Operação falhou!. Numero máximo de saques realizados")
        
        elif valor_saque > 0:
            saldo_conta -= valor_saque
            extrato +=f"Saque: R$ {valor_saque:.2f}\n"
            n_saques += 1

        else:
            print("Operação falhou!. O valor informado é invalido")
    
    elif opcao == '3':
        print("\n=========EXTRATO=======")
        print("Sem transições." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
    
    elif opcao == '4':
        break
    
    else:
        print('Operação inválida, selecione novamente a opção desejada.')