"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7


numero_cpf = input('Digite: ')
CPF_limpo = []

for indice in numero_cpf:
    if indice != '.' and indice != '-':
        CPF_limpo.append(indice)

CPF_limpo = CPF_limpo[:-2]

soma = 0
cont = 10
for digito in CPF_limpo:
    mult = cont * int(digito)
    soma += mult
    cont -= 1

r1 = soma * 10
r2 = r1 %11

if r2 > 9:
    print("0")
else:
    print(r2)

if r2 == int(CPF_limpo[0]):
    print(f'O CPF {numero_cpf} e Valido')
else:
    print('Nao e valido')

"""
cpf = '74682489070'

nove_digitos = cpf[:9]

cont = 10
soma = 0
for indice in nove_digitos:
    mult = int(indice) * int(cont)
    soma +=mult
    cont-=1
print(soma)

div = (soma * 10) % 11

div = div if div <=9 else 0
print(div)