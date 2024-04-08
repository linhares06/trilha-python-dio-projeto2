LIMITE = 500
LIMITE_SAQUES = 3

TAMANHO_DATA_NASCIMENTO = 8
TAMANHO_CPF = 11

def menu():
    menu = '''
[1] Criar Usuario
[2] Criar Conta Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar Usuarios
[7] Listar Contas Correntes
[0] Sair

Opção: '''

    return input(menu)

def main():

    extrato = ''
    saldo = 0
    numero_saques = 0

    usuarios = []
    contas_correntes = []

    while True:

        opcao = menu()

        if opcao == '1':
            criar_usuario(usuarios)

        elif opcao == '2':
            criar_conta_corrente(contas_correntes, usuarios)

        elif opcao == '3':
            saldo, extrato = deposito(extrato, saldo)

        elif opcao == '4':
            extrato, saldo, numero_saques = saque(extrato=extrato, saldo=saldo, numero_saques=numero_saques)

        elif opcao == '5':
            ver_extrato(extrato, saldo=saldo)
        
        elif opcao == '6':
            listar_usuarios(usuarios)

        elif opcao == '7':
            listar_contas_correntes(contas_correntes)

        elif opcao == '0':
            print('Sair')
            break

        else:
            print('Operação inválida, por favor selecione novament a operação desejada.')

def deposito(extrato, saldo, /):
    
    try:
        print('Deposito')

        valor = float(input('Quantia: '))

        if valor <= 0:
            print('Apenas valores maiores do que 0 são permitidos.')
        else:
            saldo += valor
            extrato += f'Deposito de R${valor:.2f}\n'
    
    except ValueError:
        print('Apenas valores numericos são permitidos.')

    return saldo, extrato

def saque(*, extrato, saldo, numero_saques):

    if numero_saques >= LIMITE_SAQUES:
        print('Limite de saque diário atingido.')

    else:
        try:
            print('Saque')

            valor = float(input('Quantia: '))
            
            if valor <= 0:
                print('Apenas valores maiores do que 0 são permitidos.')

            elif valor <= LIMITE:
                if valor > saldo:
                    print('Saldo insuficiente.')
                else:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f'Saque    de R${valor:.2f}\n'

            else:
                print(f'O valor do saque é maior do que o limite de R${LIMITE} por saque.')
      
        except ValueError:
             print('Apenas valores numericos são permitidos.')

    return extrato, saldo, numero_saques

def ver_extrato(extrato, /, *, saldo):
    print('Extrato')
    print(extrato)
    print(f'Saldo:      R${saldo:.2f}')

def validar_digitos(entrada, tamanho):
        while True:
            digitos = input(entrada)

            if digitos.isdigit() and len(digitos) == tamanho:
                digitos_validos = digitos
                break
            else:
                print(f"Entrada inválida. Certifique-se de inserir apenas números e ter {tamanho} dígitos.")

        return digitos_validos
    
def verificar_cpf_existente(cpf, usuarios):
    return [usuario for usuario in usuarios if usuario['cpf'] == cpf]

def criar_usuario(usuarios):

    print('***Criação de usuario do sistema bancario***\n')
    
    cpf = validar_digitos('Insira o CPF: ', TAMANHO_CPF)

    if not verificar_cpf_existente(cpf, usuarios):
        nome = input('Insira o nome do usuário: ')
        nascimento = validar_digitos('Insira a data de nascimento: ', TAMANHO_DATA_NASCIMENTO)
        endereco = input('Insira o endereco(Logradouro, nr - bairro - cidade/estado): ')

        usuario = {
            'nome': nome,
            'cpf': cpf,
            'nascimento': nascimento, 
            'endereco': endereco,
        }
        
        usuarios.append(usuario)
        print('Usuário criado com sucesso!')

    else:
        print('CPF já cadastrado.')

def criar_conta_corrente(contas_correntes, usuarios):

    AGENCIA = '0001'

    def gerar_numero_conta():
        if not contas_correntes:
            return 1
        else:
            return contas_correntes[-1]['numero'] + 1

    print('***Criação de conta corrente para o usuário do sistema bancario***\n')
    
    cpf = validar_digitos('Insira o CPF do usuário: ', TAMANHO_CPF)

    usuario = verificar_cpf_existente(cpf, usuarios)

    if usuario:

        conta_corrente = {
            'cpf': cpf,
            'agencia': AGENCIA,
            'numero': gerar_numero_conta(),
            'nome': usuario[0]['nome'],
        }

        contas_correntes.append(conta_corrente)
        print('Conta corrente criada com sucesso!')

    else:
        print('Usuário não cadastrado.')

def listar_usuarios(usuarios):

    print('Lista de usuários: \n')
    
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Nascimento: {usuario['nascimento']}")
            print(f"Endereço: {usuario['endereco']} \n")
    else:
        print('Nenhum usuario cadastrado.')


def listar_contas_correntes(contas_correntes):
    print('Lista de contas correntes: \n')
    
    if contas_correntes:
        for conta in contas_correntes:
            print(f"Agência: {conta['agencia']}, Número: {str(conta['numero'])}, Nome: {conta['nome']}")
        print("\n")
    else:
        print('Nenhuma conta corrente cadastrada.')

main()