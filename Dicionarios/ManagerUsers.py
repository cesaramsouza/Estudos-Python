from Dicionarios.Funcoes import *

usuarios={}
acao=perguntar()

while acao=="I" or acao=="E" or acao=="L" or acao=="P":
    if acao=="I":

        inserir(usuarios)

    elif acao=="E":
        print('teste')
    elif acao=="L":
        print('teste')
    elif acao=="P":
        login=input("Informe o usuário para busca: ").upper()
        pesquisar(usuarios,login)
    acao = perguntar()