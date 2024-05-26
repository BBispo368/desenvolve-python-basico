# Leitura de Dados

valor = int(input())

# Processamento

nota_100 = valor // 100
valor = valor - nota_100 * 100

nota_50 = valor // 50
valor = valor - nota_50 * 50

nota_20 = valor // 20
valor = valor - nota_20 * 20

nota_10 = valor // 10
valor = valor - nota_10 * 10

nota_5 = valor // 5
valor = valor - nota_5 * 5

nota_2 = valor // 2
valor = valor - nota_2 * 2

nota_1 = valor // 1

# Resultado

print(nota_100, "nota(s) de R$100,00")
print(nota_50, "nota(s) de R$50,00")
print(nota_20, "nota(s) de R$20,00")
print(nota_10, "nota(s) de R$10,00")
print(nota_5, "nota(s) de R$5,00")
print(nota_2, "nota(s) de R$2,00")
print(nota_1, "nota(s) de R$1,00")