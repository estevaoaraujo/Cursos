"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''
numero_int = input("Digite número: ")

numero_int = int(numero_int)

if numero_int % 2 == 0:
    print(f" Voce digitou {numero_int} e par")
else:
    print(f"Voce digitou {numero_int} e impar")    

'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Quantas horas: ")

horario = float(horario)

if horario > 0 and horario < 11:
    print(f" {horario}, bom dia!!!!")

elif horario < 12 and horario > 17:
    print(f" {horario}, boa tarde!!!!")

elif horario < 18 and horario > 23:
    print(f" {horario}, boa noite!!!!")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")

quantidade_letras = len(nome)

if quantidade_letras <= 4:
    print("Seu nome é curto.")
elif 5 <= quantidade_letras <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")