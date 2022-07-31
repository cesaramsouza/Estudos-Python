with open("primeiro_arquivo.txt","r") as arquivo:
    for linhas in arquivo.readlines():
        print(linhas)