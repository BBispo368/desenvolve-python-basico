import random

lista = []
menu = 0
print("Digite os itens da lista. Caso queira cancelar, aperte somente o enter")
while menu != None:
    x = input()
    if x == '':
        break
    lista.append(x)

print(lista)
print(lista[0:3])
print(lista[:-3:-1])
print(lista[::-1])
print(lista[0::2])
print(lista[1::2])