# ordenando lista

lista = [
    ['p1',13],
    ['p2',6],
    ['p3',7],
]

#altera a lista
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

#não altera a lista
print(sorted(lista, key=lambda item: item[1]))