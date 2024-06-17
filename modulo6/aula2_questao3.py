import random

lista1=[]
lista2=[]
interseccao=[]

# Gerador de lista
for i in range(20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

for i in range(20):
    for j in range(20):
        if lista1[i] == lista2[j]:
            if interseccao.count(lista1[i]) < 1:
                interseccao.append(lista1[i])

print(lista1)
print(lista2)
print(interseccao)

for i in range(len(interseccao)):
    print(f"{interseccao[i]} : Lista 1 = {lista1.count(interseccao[i])}, Lista 2 = {lista2.count(interseccao[i])}")