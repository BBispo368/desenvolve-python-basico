import math
import random

soma = 0

n = int(input())

for i in range(n):
    x = random.randint(0,100)
    soma += x
    print(x)

print(f"Resultado = {math.sqrt(soma)}")