primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite outro valor: '))

if primeiro_valor < segundo_valor:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
elif primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
else:
    print('São iguais')



