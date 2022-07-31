frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_usuario = input('Qual letra deseja mudar para maiúscula ?')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)

# while contador < tamanho_frase:
#     if contador == '0':
#         nova_string += string.upper(frase[contador])
#     else:
#         nova_string += frase[contador]
#     contador += 1
#
# print(f'teste {nova_string}')
