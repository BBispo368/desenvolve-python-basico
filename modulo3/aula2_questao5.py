# Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

#Leitura de Dados
genero = input("Escreva seu gênero ( M / F): ")
idade = int(input("Digite sua idade: "))
trabalho = int(input("digite em anos seu tempo de contribuição: "))

#Saída de Dados
print((genero == "F" and idade >= 60 or genero == "M" and idade >= 65) or (trabalho >= 30) or (idade >= 60 and trabalho >= 25))