"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')


lista = ['1', '2', '3']
tabela = ''
tamanho_lista = len(lista) # Pega o tamanho da lista

for i, item in enumerate(lista):
    tabela += item # Adiciona o número
    # Adiciona o traço, exceto se for o último item da lista
    if i < tamanho_lista - 1:
        tabela += '-'

print(tabela)