equipamentos = ['impressora','impressora','pc','teclado','mouse' ]
valores = [200,100,4000,30,25]
seriais = ['01','02','03','04','05']
departamentos = ['TI','TI','TI','TI','TI']
resposta = "S"

print("Quantidade? ",len(equipamentos))
for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
  print("--------------------------------------")

busca=input("Digite o nome do equipamento que sera depreciado: ").lower()

for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    if equipamentos[indice]=='impressora':
      valores[indice]=valores[indice]-(valores[indice]*0.1)
      print("Valor..: ",valores[indice])
      print("Serial.:", seriais[indice])
    else:
      print("Valor..: ", valores[indice])
      print("Serial.:", seriais[indice])