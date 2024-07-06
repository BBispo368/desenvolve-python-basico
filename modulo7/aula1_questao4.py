telefone = input("Digite o numero: ")
if len(telefone) < 9: telefone = "9" +telefone
print(telefone[:5]+"-"+telefone[5:])