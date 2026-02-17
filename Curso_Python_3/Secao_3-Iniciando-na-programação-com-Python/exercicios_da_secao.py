"""
================================================================================
  EXERCÍCIOS - SEÇÃO 3 - INICIANDO NA PROGRAMAÇÃO COM PYTHON
  Resolva os 5 exercícios abaixo. Não há respostas prontas: faça você mesmo!
================================================================================
"""

def menu():
    
    while True:
        op = int(input('opção: '))
        if 1 == op:
            ex1()
        if 2 == op:
            ex2()
        if 3 == op:
            ex3()
        if 4 == op:
            ex4()
        if 5 == op:
            ex5()
        if 6 == op:
            print('Saindo....')
            break


def ex1():

    # =============================================================================
    # EXERCÍCIO 1 - Variáveis, input e operadores aritméticos
    # =============================================================================
    # Peça ao usuário: nome, altura (em metros) e peso (em kg).
    # Calcule o IMC (peso / altura²) e exiba uma mensagem usando f-string no formato:
    # "(nome) tem (altura)m, pesa (peso)kg e seu IMC é (imc)"
    # Dica: use input(), float(), e a fórmula IMC = peso / (altura * altura)
    # -----------------------------------------------------------------------------
    # Seu código aqui:

    nome = 'Estevao'
    altura = float(1.84)
    peso = float(100)

    IMC = peso / altura ** 2

    print(f'{nome} tem {altura}, pesa {peso} e eu IMC é {IMC}')


def ex2():
    # =============================================================================
    # EXERCÍCIO 2 - Condicionais (if / elif / else)
    # =============================================================================
    # Peça dois números ao usuário. Mostre qual é o maior, qual é o menor,
    # ou se são iguais. Use apenas if, elif e else (e operadores de comparação).
    # -----------------------------------------------------------------------------
    # Seu código aqui:
    n1 = int(8)
    n2 = int(4)

    if n1 > n2:
        print(f'maior {n1}')
        print(f'menor {n2}')
    else:
        print(f'maior {n2}')
        print(f'menor {n1}')

def ex3():        
    # =============================================================================
    # EXERCÍCIO 3 - Operadores lógicos (and / or)
    # =============================================================================
    # Simule um login: peça usuário e senha. Defina um usuário e senha corretos
    # em variáveis. Se usuário E senha estiverem corretos, imprima "Acesso liberado".
    # Caso contrário, imprima "Usuário ou senha incorretos."
    # -----------------------------------------------------------------------------
    # Seu código aqui:

    print('##################################################')
    print('################### BEM VINDO ####################')
    print('##################################################')

    login ='Estevao'
    senha = 142563

    log = 'Estevao'
    sen = 142563

    if login == log:
        
        if senha == sen:
            print('Login com sucesso')
        else:
            print('Senha invalido')
    else:
        print('Login invalidos')

def ex4():
    # =============================================================================
    # EXERCÍCIO 4 - while e break
    # =============================================================================
    # Use um loop while para pedir números ao usuário. Some todos os números
    # digitados. Quando o usuário digitar 0, saia do loop (break) e mostre
    # a soma total dos números digitados (sem contar o 0).
    # -----------------------------------------------------------------------------
    # Seu código aqui:
    
    cal = []
    while True:
        escolha = input("Deseja continuar S/N:")
        if 'S' == escolha:
            valor = int(input('Valor: '))
            cal.append(valor)
        else:
            print("Saindo...")
            break

    print(f'Total: {sum(cal)}, valores {cal}' )    

        
def ex5():
    # =============================================================================
    # EXERCÍCIO 5 - for, listas e range (ou enumerate)
    # =============================================================================
    # Crie uma lista com pelo menos 4 nomes. Use um for para exibir cada nome
    # com seu índice, no formato: "0 - Maria", "1 - João", etc.
    # Dica: use for com range(len(lista)) ou for com enumerate(lista).
    # -----------------------------------------------------------------------------
    # Seu código aqui:
    Lista = ['Estevao','Natanael','Daniel','joao']

    for indice, list in enumerate(Lista):
        print(f'Posição {indice}: {list}')
    
    # =============================================================================
    # FIM DOS EXERCÍCIOS - Boa prática!
    # =============================================================================


menu()