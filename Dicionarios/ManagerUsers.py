from Dicionarios.Funcoes import *

usuarios={}
acao=perguntar()

while acao=="I" or acao=="E" or acao=="L" or acao=="P" or acao=="S":
    if acao=="I":

        inserir(usuarios)

    elif acao=="E":

        login = input("Informe o usuário a ser excluído: ").upper()
        deletar(usuarios,login)

    elif acao=="L":

        listar(usuarios)

    elif acao=="P":

        login=input("Informe o usuário para busca: ").upper()
        pesquisar(usuarios,login)

    elif acao=="S":

        salvar(usuarios)

    acao = perguntar()