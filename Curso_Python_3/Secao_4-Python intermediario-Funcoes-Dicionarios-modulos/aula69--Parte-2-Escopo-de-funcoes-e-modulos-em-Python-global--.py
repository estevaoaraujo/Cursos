x = 1

y=x

def escopo():
    global y
    y = 2
    print(y)
    z = y

    def outro():
        global z
        z = 9
        print(z)
    outro()
escopo()
print(x)
print(y)