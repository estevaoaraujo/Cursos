def numeros_gerador():
    for i in range(1, 6):
        yield i   # << yield transforma a função num generator

for n in numeros_gerador():
    print(n)



def numeros_lista():
    return [1, 2, 3, 4, 5]

for n in numeros_lista():
    print(n)
