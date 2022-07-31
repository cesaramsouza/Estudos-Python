def perguntar():
    resposta = input(' "I" - Inserir um usuário \n "E" - Excluir um usuário \n "L" - Listar o usuário \n "P - Pesquisar usuário \n Aperte "ENTER" para finalizar \n O que deseja fazer?').upper()
    return resposta

def inserir(dicionario):
    login=input("Digite o login: ").upper()
    dicionario[login] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario,chave):
    lista=dicionario.get(chave)
    if chave != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])