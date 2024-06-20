
import random
lista = []
for i in range(20):
    lista.append(random.randint(-10,10))

print("Original:", lista)

# Encontrar o intervalo com a maior quantidade de números negativos
max_neg_count = 0
max_neg_inicio = 0
max_neg_fim = 0

atual_neg_count = 0
atual_neg_inicio = 0

for i in range(len(lista)):
    if lista[i] < 0:
        if atual_neg_count == 0:
            atual_neg_inicio = i
        atual_neg_count += 1
    else:
        if atual_neg_count > max_neg_count:
            max_neg_count = atual_neg_count
            max_neg_inicio = atual_neg_inicio
            max_neg_fim = i
        atual_neg_count = 0

# Verificar se o último intervalo é o maior
if atual_neg_count > max_neg_count:
    max_neg_count = atual_neg_count
    max_neg_inicio = atual_neg_inicio
    max_neg_fim = len(lista)

# Deletar o intervalo com a maior quantidade de números negativos
del lista[max_neg_inicio:max_neg_fim]

print("Editada: ", lista)