nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
altura = float(input('Qual sua altura? '))
peso =  int(input('Qual seu peso? '))
ano = int(input('Ano? '))
dt_nasc = ano - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura pesa {peso}KG')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {dt_nasc}')

if imc >= 18.5 and imc <= 24.9:
    print('Ok! Pode comer')
elif imc >= 25:
    print('GORDÃO')
