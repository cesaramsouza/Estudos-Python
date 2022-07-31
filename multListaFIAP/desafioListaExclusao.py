equipamentos = ['impressora','impressora','pc','teclado','mouse' ]
valores = [200,100,4000,30,25]
seriais = ['01','02','03','04','05']
departamentos = ['TI','TI','TI','TI','TI']
resposta = "S"

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
  print("--------------------------------------")

busca=input("Digite o serial do equipamento que deseja remover: ").lower()

for indice in range(0,len(equipamentos)):
  if busca==seriais[indice]:
    del equipamentos[indice]
    del valores[indice]
    del departamentos[indice]
    del seriais[indice]
    break

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
  print("--------------------------------------")