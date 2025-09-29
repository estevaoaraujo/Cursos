'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''

def primos (self):
    numero = self
    cont = 1
    primo = []
    primo_bol = True

    while  cont <= numero :
        if (numero % cont) == 0:
            primo.append(cont)
            primo_bol = primo_bol if len(primo) <=2 else False

        cont +=1

    print(primo_bol)
    print(primo)



dado = int(input('Digite primo: '))
primos(dado)