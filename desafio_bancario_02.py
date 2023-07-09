##################################################
#           Importação de bibliotecas:
#
# 1 - OS
#   limpar a tela via a linha de comando  
#   No Windows 'cls' 
#
# 2 - TextWrap
#   Organiza saída de texto  
##################################################
import os

import textwrap

##################################################
#                    Funções:
##################################################

# Funções de Validação:
##################################################

def validar_valor(valor):
    try:
        float(valor)
    except ValueError:
        return False
    return True

def validar_cpf(cpf):
    try:
        int(cpf)
    except ValueError:
        return False
    return True

def filtrar_usuario(cpf, novo_usuario):
    usuarios_encontrado = [procurado for procurado in novo_usuario if procurado["cpf"] == cpf]
    return usuarios_encontrado[0] if usuarios_encontrado else None
    
# Funções básicas do sistema:
##################################################

def exibir_menu():
    # os.system('cls')
    menu = """====== Digite uma opção [?] ======
Básico:
\t[ D ] Depositar
\t[ S ] Sacar
\t[ E ] Extrato

Gerenciamento:
\t[ C ] novo Cliente
\t[ L ] Listar clientes
\t[ T ] nova conTa
\t[ O ] listar cOntas

\t[ r] saiR
==================================

=> Opção: """
    return input(textwrap.dedent(menu)).lower()

def depositar(saldo_atual, deposito, extrato_atual, /,):
    
    reais = f'{deposito:_.2f}'
    reais = reais.replace('.', ',').replace('_','.')

    if deposito > 0:
        saldo_atual += deposito
        extrato_atual += f"Depósito: R$ {reais}\n"
        print('\n'+ '=' * 32)
        print(f'Depósito de R$ {reais} realizado')
        input('Aperte [ENTER] para continuar')        
        os.system('cls')

    else:
        print('\n'+ '=' * 32)
        print("Operação inválida! Valore não reconhecido.")
        input('Aperte ENTER para continuar')
        os.system('cls')

    return saldo_atual, extrato_atual

def sacar(*,numero_de_saques, saque_desejado, saldo_atual, lim_por_saque, lim_saques_diario, extrato_atual):  
    
    reais = f'{saque_desejado:_.2f}'
    reais = reais.replace('.', ',').replace('_','.')   
    
    if numero_de_saques >= lim_saques_diario:
        print('\n'+ '=' * 32)
        print(F"Não é possível concluir a operação! Sua conta só permite {lim_saques_diario} saques diários.")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
    elif saque_desejado > saldo_atual:
        print('\n'+ '=' * 32)
        print("Não é possível concluir a operação! Saldo insuficiente.")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
    elif saque_desejado > lim_por_saque:
        print('\n'+ '=' * 32)
        print(f"Não é possível concluir a operação. O limite por saque atual é R$ {lim_por_saque:.2f}")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
    elif saque_desejado > 0:
        saldo_atual -= saque_desejado
        extrato_atual += f"Saque:    R$ {reais}\n"
        numero_de_saques += 1      

        print('\n'+ '=' * 32)
        print(f"operação concluída com sucesso!\nSaque de R$ {reais} realizado.")            
        input('Aperte [ENTER] para continuar')
        os.system('cls')

    return saldo_atual, extrato_atual, numero_de_saques

def exibir_extrato(extrato_atual,/,*, saldo_atual):
        os.system('cls')
        reais = f'{saldo_atual:_.2f}'
        reais = reais.replace('.', ',').replace('_','.') 

        print("================== EXTRATO ==================\n")       
        print("Não foram realizadas movimentações.\n" if not extrato_atual else extrato_atual)
        print(f"\nSaldo:    R$ {reais}")
        print('=' * 45)
        input('\nAperte [ENTER] para continuar')
        os.system('cls')

def criar_cliente(cliente_atuais):
# Receber e validar o CPF
    cpf = input("Informe o CPF (somente números): ")
    os.system('cls')
    if not validar_cpf(cpf):
        print(f'O CPF = "{cpf}" não é válido')
        print("==========================================")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
        return
    
# Verificar se já existe cliente com o CPF   
    usuario_ja_existe = filtrar_usuario(cpf, cliente_atuais)
        
    if usuario_ja_existe:
        print(f"\nCliente já cadastrado com o CPF = {cpf}\n")
        print("==========================================")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
        return    
    
# Criar novo cliente
    nome = input("Informe o nome completo do novo cliente: ")
    os.system('cls')

# Data de nascimento
    dia_nascimento = input("Informe o dia do nascimento com dois dígitos (dd): ")
    os.system('cls')
    mes_nascimento = input("Informe o mês do nascimento com dois dígitos (mm): ")
    os.system('cls')
    ano_nascimento =  input("Informe o ano do nascimento com quatro dígitos (aaaa): ")
    os.system('cls')

# Endereço
    logradouro = input("Informe o logradouro: ")
    os.system('cls')
    numero = input("Informe o número: ")
    os.system('cls')
    bairro = input("Informe o bairro: ")
    os.system('cls')
    cidade = input("Informe a cidade: ")
    os.system('cls')
    sigla_estado = input("Informe a sigla estado: ")   
    os.system('cls')

    cliente_atuais.append({
        "nome": nome, 
        "cpf": cpf,
        "dia_nascimento": dia_nascimento,
        "mes_nascimento": mes_nascimento,
        "ano_nascimento": ano_nascimento,
        "data_nascimento": f'{dia_nascimento}-{mes_nascimento}-{ano_nascimento}', 
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "sigla_estado": sigla_estado,
        "endereco": f'{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}'})

    print("Novo cliente cadastrado com sucesso!\n")
    print("==========================================")
    input('Aperte ENTER para continuar')
    os.system('cls')

def listar_clientes(clientes_atuais):
    if not clientes_atuais:
        print('Não existem clientes cadastrados')
        print('=' * 45)
        input('\nAperte [ENTER] para continuar')
        os.system('cls')
        return
    for cliente in clientes_atuais:
        linha = f"""\
            Nome:\t\t{cliente['nome']}
            cpf:\t\t{cliente['cpf']}
            Nascimento:\t{cliente['data_nascimento']}            
        """
        print("=" * 45)
        print(textwrap.dedent(linha))
     
    print("==========================================")
    input('Aperte [ENTER] para continuar')
    os.system('cls')

def criar_conta(contas, clientes_atuais, agencia):
# Receber e validar o CPF
    cpf = input("Informe o CPF (somente números): ")
    os.system('cls')
    if not validar_cpf(cpf):
        print(f'O CPF = "{cpf}" não é válido')
        print("==========================================")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
        return

# Verificar se existe cliente cadastrado com o CPF
    usuario_ja_existe = filtrar_usuario(cpf, clientes_atuais)        
    if not usuario_ja_existe:
        print(f"\nNenhuma cliente cadastrado com o CPF = {cpf}\n")
        print("==========================================")
        input('Aperte [ENTER] para continuar')
        os.system('cls')
        return 

# Criar nova conta
    numero_conta = len(contas) + 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_ja_existe})

    print('Nova conta cadastrada com sucesso!') 
    print('=' * 45)
    input('\nAperte [ENTER] para continuar')
    os.system('cls')

def listar_contas(contas):
    os.system('cls')

    if not contas:
        print('Não existem contas cadastradas')
        print('=' * 45)
        input('\nAperte [ENTER] para continuar')
        os.system('cls')
        return
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 45)
        print(textwrap.dedent(linha))
    
    
    input('Aperte [ENTER] para continuar')
    os.system('cls')
  
def sistema_banco():
    ##################################################
    #                   Variáveis
    ##################################################
    LIMITE_POR_SAQUE = 500
    LIMITE_DIARIO_DE_SAQUES = 3
    AGENCIA = "0001"


    saldo = 0
    extrato = ""
    numero_saques = 0
    extrato = ""
    numero_saques = 0
    clientes_atuais = []
    contas = []
    ##################################################

    # Limpa o console
    os.system('cls')

    # Mensagem de boas vindas
    print('Bem-vindo ao Sistema bancário Geo 2.0\n')
    input('Aperte o [ENTER] para iniciar: ')    

    while True: 

        resposta = exibir_menu()        
       
        if resposta == "r":
            os.system('cls')
            confirmar = input('''Deseja realmente SAIR?

[S] para sair

[ENTER] para retornar ao Menu Inicial

Opção => ''').lower()
            if confirmar == 's':
                os.system('cls')
                exit()
        
        elif resposta == "d":
            os.system('cls')

            deposito_desejado = (input("Informe o valor do depósito: "))

            if validar_valor(deposito_desejado):
                deposito_desejado = float(deposito_desejado)
                saldo, extrato = depositar(saldo, deposito_desejado, extrato)
            else:
                print(f'\nO valor digitado "{deposito_desejado}" não é valido\n')
                input('Digite ENTER para retornar ao Menu Inicial: ')    

        elif resposta == 's':
            os.system('cls')

            saque_desejado = (input("Informe o valor em reais que deseja sacar: "))

            if validar_valor(saque_desejado):
                saque_desejado = float(saque_desejado)
                if saque_desejado > 0:
                    saldo, extrato, numero_saques = sacar(
                        numero_de_saques = numero_saques, 
                        saque_desejado = saque_desejado,
                        saldo_atual = saldo,
                        lim_por_saque = LIMITE_POR_SAQUE,
                        lim_saques_diario = LIMITE_DIARIO_DE_SAQUES,
                        extrato_atual = extrato
                        )
            else:
                print(f'\nO valor digitado "{saque_desejado}" não é valido\n')
                input('Digite ENTER para retornar ao Menu Inicial: ') 

        elif resposta == 'e':
            exibir_extrato(extrato, saldo_atual = saldo)

        elif resposta == "c":
            os.system('cls')
            criar_cliente(clientes_atuais)
        elif resposta == "l":
            os.system('cls')
            listar_clientes(clientes_atuais)

        elif resposta == "t":
            os.system('cls')
            criar_conta(contas, clientes_atuais, AGENCIA)

        elif resposta == 'o':
            listar_contas(contas)

# Início do programa
# Chamada da função principal
sistema_banco()    
