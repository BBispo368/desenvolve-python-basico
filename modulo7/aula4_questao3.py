import os
f = open('estomago.txt')
palavras = f.read()
f.close()
f = open('estomago.txt')
linhas = f.readlines()

print(" ".join(linhas[:25]))
print(f"O documento tem {len(linhas)} linhas")

maior = 0
maior_indice = 0

for i in range(len(linhas)):
    if len(linhas[i]) > maior:
        maior = len(linhas[i])
        maior_indice = i
print(f"Maior linha é a de indice {maior_indice}")

nonato = palavras.count("Nonato") + palavras.count("nonato")
iria = palavras.count(" Íria") + palavras.count(" íria")

print(f"Nonato apareceu {nonato} vezes")
print(f"Íria apareceu {iria} vezes")

