import random

n = random.randint(1,10)
elementos = []
for i in range(n):
    num_elementos = random.randint(5,20)
    elementos.append(num_elementos)
print(elementos)
print(sum(elementos))
print(sum(elementos)/n)