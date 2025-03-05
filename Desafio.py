from datetime import datetime
import textwrap


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!\n")
        return

    nome = input("Informe o nome: ")
    data_de_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    logradouro = input("Informe o logradouro do endereço: ")
    numero = input("Informe o número do endereço: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado UF: ")

    endereco = {
        "logradouro": logradouro,
        "numero": int(numero),
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }

    novo_usuario = {
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("\n✅ Usuário cadastrado com sucesso!\n")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        nova_conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0.0,
            "extrato": ""
        }
        print("\n=== Conta criada com sucesso! ===")
        return nova_conta

    print("\n=== Usuário não encontrado, fluxo de criação de conta encerrado. ===")
    return None


def lista_contas(contas):
    for conta in contas:
        linha = f"""\   
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}       
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def menu():
    print("\n===== MENU =====")
    print("[0] Depositar")
    print("[1] Sacar")
    print("[2] Extrato")
    print("[3] Novo usuário")
    print("[4] Nova conta")
    print("[5] Listar contas")
    print("[6] Sair")
    return input("Escolha uma opção: ")


def depositar(saldo, valor, extrato, transacoes_diarias, limite_transacoes):
    if transacoes_diarias >= limite_transacoes:
        print("\n@@@ Operação falhou! Você excedeu o número de transações diárias. @@@")
        return saldo, extrato, transacoes_diarias

    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato += f"{data_hora} - Depósito:\tR$ {valor:.2f}\n"
        transacoes_diarias += 1
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato, transacoes_diarias


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, transacoes_diarias, limite_transacoes):
    if transacoes_diarias >= limite_transacoes:
        print("\n@@@ Operação falhou! Você excedeu o número de transações diárias. @@@")
        return saldo, extrato, numero_saques, transacoes_diarias

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato += f"{data_hora} - Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        transacoes_diarias += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques, transacoes_diarias


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def main():
    limite_saques = 3
    agencia = '0001'
    limite_transacoes_diarias = 10
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    transacoes_diarias = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor do depósito em R$: "))
            saldo, extrato, transacoes_diarias = depositar(saldo, valor, extrato, transacoes_diarias,
                                                           limite_transacoes_diarias)

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques, transacoes_diarias = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
                transacoes_diarias=transacoes_diarias,
                limite_transacoes=limite_transacoes_diarias
            )

        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "3":
            criar_usuario(usuarios)

        elif opcao == "4":
            conta = criar_conta(agencia, contas, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            lista_contas(contas)

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
