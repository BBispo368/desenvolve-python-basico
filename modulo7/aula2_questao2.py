frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
for i in range(len(vogais)):
    frase = frase.replace(vogais[i],"*")
print(frase)