lista1 = []
lista2 = []
lista3 = []

len1 = int(input("Digite a quantidade de elementos da lista 1: "))
for i in range(len1):
    lista1.append(int(input()))

len2 = int(input("Digite a quantidade de elementos da lista 2: "))
for i in range(len2):
    lista2.append(int(input()))

maior = lambda a,b:a>b
if maior(len1,len2):
    len3 = len1
else:
    len3 = len2

for i in range(len3):
    if i >= len1:
        lista3.append(lista2[i])
    else:
        lista3.append(lista1[i])
        lista3.append(lista2[i])
print(lista3)