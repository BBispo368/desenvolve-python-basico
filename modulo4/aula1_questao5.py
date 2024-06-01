n = int(input("Quantidade de pessoas: "))
soma = 0
cont = 0

while cont < n:
    idade = int(input("Digite a idade: "))
    soma += idade
    cont += 1
print("Media: ",soma / n)
