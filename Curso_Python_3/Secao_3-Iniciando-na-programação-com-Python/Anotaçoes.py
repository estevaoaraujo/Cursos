"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

'''Para conta de quantos elementos tem na lista usamos o len()'''
tabela = ['','1','2','3','4','5','6','7','8','9','10']
contagem = tabela.count('2')
print(f"O valor '2' aparece {contagem} vezes na lista.")