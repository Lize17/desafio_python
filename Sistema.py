import textwrap

def menu():

    menu = """\n
    ============== MENU =============
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo usúario
    [7] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo_conta, valor_deposito, extrato,/):
    if valor_deposito > 0:
        saldo_conta += valor_deposito
        extrato +=f"Depósito: R$ {valor_deposito:.2f}\n"
        print("DEPOSITADOOOOO!!")
    else:
        print("Operação falhou!. O valor informado é invalido")
    return saldo_conta,extrato

def sacar(*, saldo_conta, valor_saque, extrato, limite, n_saques, LIMITE_SAQUES):

        if valor_saque > saldo_conta:
            print("Operação falhou!. Saldo insuficiente")
        
        elif valor_saque > limite:
            print("Operação falhou!. O valor do saque ultrapassa o limite")
        
        elif n_saques >= LIMITE_SAQUES:
            print("Operação falhou!. Numero máximo de saques realizados")
        
        elif valor_saque > 0:
            saldo_conta -= valor_saque
            extrato +=f"Saque: R$ {valor_saque:.2f}\n"
            n_saques += 1

        else:
            print("Operação falhou!. O valor informado é invalido")
        return saldo_conta, extrato

def exibir_extrato(saldo_conta,/,*,extrato):
    print("\n=========EXTRATO=======")
    print("Sem transições." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")

def novo_usuario(usuarios):
    cpf = input("Informe o seu CPF, contendo apenas números: ")
    usuarios = filtrar_usuarios(cpf, usuarios)

    if usuarios:
        print("CPF já cadastrado!!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nasci = input("Informe sua data de nascimento no formato (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço no formato (lograduro, nro - bairro - cidade/uf)")

    usuarios.append({"nome": nome, "data_nascimento": data_nasci, "CPF": cpf, "Endereço": endereco})

    print("ADD COM SUCESSSO!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    '''usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)'''
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, n_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta Criado com SUcesso!!")
        return({"Agencia": agencia, "Numero_Conta": n_conta, "usuario": usuario})
    
    print("Usuário não encontrado, fluxo encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['n_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo_conta = 0 
    limite = 500
    extrato = ""
    n_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':

            valor_deposito = float(input("Informe o valor do deposito: "))

            saldo_conta,extrato = depositar(saldo_conta, valor_deposito, extrato)
        
        elif opcao == '2':
            valor_saque = float(input("Informe o valor do saque: "))

            saldo_conta, extrato = sacar(
                saldo_conta = saldo_conta,
                valor_saque = valor_saque,
                extrato = extrato,
                limite = limite,
                n_saques = n_saques,
                LIMITE_SAQUES = LIMITE_SAQUES
            )
        
        elif opcao == '3':
            exibir_extrato(saldo_conta,extrato=extrato)

        elif opcao == '4':
            n_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,n_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            novo_usuario(usuarios)

        elif opcao == '7':
            break
        
        else:
            print('Operação inválida, selecione novamente a opção desejada.')

main()