import json

with open("bd.json") as arq_json:
    dic = json.load(arq_json)

    for chave, dados in dic.items():
        print(chave+" "+str(dados))