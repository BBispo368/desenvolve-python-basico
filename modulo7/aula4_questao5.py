import os,random

with open("gabarito_forca.txt",'r') as f: palavras = f.read()

palavras = palavras.split()
palavra = palavras[random.randint(0,9)]

print("Tamanho: :", len(palavra))

palavra_enforcado = ["*" for i in range(len(palavra))]
f = open("gabarito_enforcado.txt",'a')
while "".join(palavra_enforcado) != palavra:
    print("".join(palavra_enforcado))
    f.write("".join(palavra_enforcado)+'\n')
    tentativa = input("Digite uma letra: ")
    if palavra.count(tentativa) > 0:
        for i in range(len(palavra)):
            if palavra[i] == tentativa: palavra_enforcado[i] = tentativa
f.close()
print("".join(palavra_enforcado))