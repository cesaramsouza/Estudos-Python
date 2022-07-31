usuarios={}
buscaUser = "S"
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"],
    "Florinda":["Florinda Flores", "26/11/2017", "Recep_01"]
    }

print(usuarios)
print("##############========#########")
while buscaUser == "S":
    busca=input("Digite o usuário que quer visualizar os dados: ")
    print("Dados: ",usuarios.get(busca))
    buscaUser=input("Se deseja procurar mais usuários, digite \"S\": ").upper()