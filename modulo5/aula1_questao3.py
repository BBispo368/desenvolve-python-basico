from operator import truediv
import random

x = random.randint(1,10)
palpite = False

while palpite == False:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    if chute > x:
        print("Muito alto, tente novamente")
        continue
    elif chute < x:
        print("Muito baixo, tente novamente")
        continue
    else:
        print(f"Correto! O número é {x}")
        palpite = True