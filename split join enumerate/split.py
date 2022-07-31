#split - dividir uma string

string = 'O Brasil é o pais do futebol, o Brasil é penta'

lista1 = string.split(' ')
lista2 = string.split(',')

contagem = 0
qtd_vezes = 0
palavra = ''

for valor in lista1:
    #print(f'A palavra {valor} apareceu {lista1.count(valor)} vezes')
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra {palavra} foi a que mais se repetiu, ({contagem}x)')