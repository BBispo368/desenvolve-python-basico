# Leitura de Dados

comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
preco_m2 = float(input("Digite o valor do metro quadrado: "))

# Processamento de Dados

area_m2 = comprimento * largura
preco_total = preco_m2  * area_m2

# Resultado

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")