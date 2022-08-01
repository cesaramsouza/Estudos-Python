with open("iris.data","r") as arquivo:
    baseDados = []
    for registro in arquivo.readlines():
        baseDados.append(registro.split(","))
        
print(float(baseDados[0][0])+float(baseDados[0][1]))