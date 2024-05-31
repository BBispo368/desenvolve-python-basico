distancia = int(input("Digite a distância em km: "))
peso = float(input("Digite o peso em kg: "))

if distancia  <= 100:
    preco = 1 * peso
if 100 < distancia <= 300:
    preco = 1.5 * peso
else:
    preco = 2*peso
if peso > 10:
    preco = preco + 10

print(f"frete: R${preco:,.2f}")