secreto = 'perfurme'
digitadas = []
chance = 3

while True:

    if chance == 0:
        print(f'As suas chances zeraram, você perdeu ! A palavra secreta era "{secreto}"')
        break
    else:
        print(f'Você tem {chance} chances')


    letra = input('Digite uma letra: ')
    letra = letra.lower()

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta')

    else:
        print(f'A letra "{letra}" não existe na palavra secreta')
        chance -= 1
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Você ganhou! A palavra era {secreto}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')