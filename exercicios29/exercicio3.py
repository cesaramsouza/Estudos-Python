nome = input('Escreva seu primeiro nome: ')

contador = len(nome)

if contador <= 4:
    print('Seu nome é curto')

elif contador <= 6:
    print('Seu nome é normal')

elif contador > 6:
    print('Seu nome é muito grande')

else:
    pass
