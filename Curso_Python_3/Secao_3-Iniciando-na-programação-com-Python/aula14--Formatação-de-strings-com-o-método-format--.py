#32. Formatação string
a = 'A'
b = 'B'
c = 1.155

formato_1 = 'a={0} b= {1} c= {2:.2f}'.format(a,b,c)
formato_2 = 'a={1} b= {0} c= {2:.2f}'.format(a,b,c)

print(formato_1)
print(formato_2)


a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)