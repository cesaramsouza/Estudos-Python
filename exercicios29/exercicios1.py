num1 = input('Digite um numero inteiro: ')

try:
    num1 = int(num1)
    div = num1 % 2

    if div == 0:
        print(f'{num1} é um número par')

    else:
        print(f'{num1} é um número ímpar')

except:
    print('Número inválido')
