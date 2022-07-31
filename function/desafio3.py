
def perc(n1,n2):
    if n2 == 0:
        return
    return n1+(n1*(n2/100))

valor = perc(27,1)

if valor:
    print(valor)
else:
    print('Erro no calculo')
    