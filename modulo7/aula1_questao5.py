frase = input("Digite a frase: ")
lista = []
for letra in "aeiouAEIOU":
    for i in range(len(frase)):
        if letra == frase[i]: lista.append(i)
print("Indices: ",sorted(lista))