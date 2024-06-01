n = int(input("n: "))
maior = 0

while n > 0:
    x = int(input(f"x ({n}): "))
    if x > maior:
        maior = x
    n -= 1

print("Maior: ", maior)