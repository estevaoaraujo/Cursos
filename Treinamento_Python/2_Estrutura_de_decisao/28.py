'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print('Supermercado Tajara')

clientes = []

nome = input('Seu nome: ')
clientes.append(nome)


carne= ['File Duplo','Alcatra','Picanha']
preco_promo =[4.90,5.90,6.90]
preco =[5.80,6.80,7.80]

print('                      Até 5 Kg           Acima de 5 Kg')
print('1 - File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('2 - Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('3 - Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')

escolha = input(f'{nome} faça seu pedido:')

if escolha == '1':
    qtd = float(input('QTD: '))
    if qtd <=5:
        print(f'Pedido:\n carne: {escolha}\nquantidade: {qtd}\nPreço:{preco_promo[0]}\ntotal: {qtd * preco_promo[0]}')
    else:
        print(f'Pedido:\n carne: {escolha}\nquantidade: {qtd}\nPreço:{preco[0]}\ntotal: {qtd * preco[0]}')

elif escolha =='2':
    qtd = float(input('QTD: '))
    if qtd <=5:
        print(f'Pedido:\n carne: {escolha}\nquantidade: {qtd}\nPreço:{preco_promo[1]}\ntotal: {qtd * preco_promo[1]}')
    else:
        print(f'Pedido:\n carne: {escolha}\nquantidade: {qtd}\nPreço:{preco[1]}\ntotal: {qtd * preco[1]}')

elif escolha =='3':
    qtd = float(input('QTD: '))
    if qtd <=5:
        print(f'Pedido:\n carne: {escolha}\nquantidade: {qtd}\nPreço:{preco_promo[2]}\ntotal: {qtd * preco_promo[2]}')
    else:
        print(f'Pedido:\n carne: {escolha}\nquantidade: {qtd}\nPreço:{preco[2]}\ntotal: {qtd * preco[2]}')