def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado no valor de R$ {valor:.2f} \n"
    else: 
        print("Valor inválido")
    return saldo, extrato
        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo o suficiente.")
    elif excedeu_limite:
        print("Você excedeu o limite.")
    elif excedeu_saque:
        print("Você excedeu o número de saques.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
    else:
        print("Valor informado inválido.")
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário antes de criar a conta.")
        return

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (Apenas números): ")
    for usuario in usuarios:    
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado")
            return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ") 
    endereco = input("Informe o endereço (logradouro, bairro, número, cidade/sigla estado): ")   
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_contas(contas):
            if not contas:
                print("Nenhuma conta cadastrada.")
            return
    
            print("\n================ LISTA DE CONTAS ================")
            for conta in contas:
                usuario = conta['usuario']
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {usuario['nome']}")
            print("-------------------------------------------------")


if __name__ == "__main__":
    menu = """

    [d] Depositar
    [s] Sacar 
    [e] Exibir Extrato
    [q] Sair 
    [u] Criar usuário
    [c] Criar conta
    [l] Listar contas
    => """ 

    saldo = 0
    numero_saques = 0 
    limite = 500
    extrato =""
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"
    numero_conta = 1  

    while True:
        opcao = input(menu)
        
        if opcao == "d":
            try:
                valor = float(input("Informe o Valor do Depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("Valor inválido")


        elif opcao == "s":
            valor = int(input("Informe o Valor do Saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
            if valor <= saldo and numero_saques < limite_saques:
                try: 
                    numero_saques += 1
              
                except ValueError:
                    print("Valor inválido")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        elif opcao == "u":  
            criar_usuario(usuarios)

        elif opcao == "c":  
            criar_conta(agencia, numero_conta, usuarios)
            numero_conta += 1  
        
        elif opcao == "l":
            listar_contas
        
        else:
            print("Opção inválida, tente novamente.")
