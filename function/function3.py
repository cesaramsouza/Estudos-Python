#args e kwards

# def func(*args):
#     for v in args:
#         print(v)
#
# func(1,2,3,4,5)

# passando a lista na função
def func(*args):
    print(args)

lista = [1,2,3,4,5]
func(*lista)

# def func(*args,**kwargs):
#     nome=kwargs.get('nome')
#     soma= args[0]+args[1]
#     divisao= args[0]/args[1]
#     multiplicacao= args[0]*args[1]
#     subtracao= args[0]-args[1]
#     resto= args[0]%args[1]
#     percent= args[0]*(args[1]/100)
#     print('soma:',soma,'divisao:',divisao,'multiplicacao:',multiplicacao,'subtracao:',subtracao,'resto:', resto,'percent:', percent, nome)

# lista=[50,5]
# func(*lista,nome='Cesar')
