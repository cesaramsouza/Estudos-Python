num1 = input('Digite o horário de 0 a 23: ')

try:
    num1 = int(num1)

    if num1 >= 0 and num1 <= 11:
        print('Bom dia')

    elif num1 >= 12 and num1 <= 17:
        print('Boa tarde')

    elif num1 >= 18 and num1 <= 23:
        print('Boa noite')
    else:
        print('Horário incorreto')

except:
    print('Número inválido')
