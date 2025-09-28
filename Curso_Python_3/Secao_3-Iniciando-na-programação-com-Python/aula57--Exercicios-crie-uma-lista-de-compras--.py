"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
ligado = True
lista =[]

while ligado:
    
    print('-----SyStem Compre------')
    print('----------Menu--------')
    print("---- 1 - Inserir compras----")
    print("---- 2 - apagar compras-----")
    print("---- 3 - listar compras-----")
    print("---- 4 - sair---------------")

    play = int(input(f'Escolha: '))

    if play == 1:
        compras = input('Insira:')
        lista.append(compras)
    
    if play == 2:
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    if play == 3:
        for indice,nome in enumerate(lista):
            print(indice,lista[indice])
    
    if play == 4:
        ligado = False
        print("bye")