import random
lista = []

for i in range(20):
    lista.append(random.randint(-100,100))
print("Ordenada: ",sorted(lista))
print("Original: ", lista)
print("Maior valor: ", max(lista))
print("Menor valor: ", min(lista))
