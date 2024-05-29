#Leitura de Dados
idade = int(input("Digite sua idade: "))
jogo = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
vitoria = int(input("Quantos jogos já venceu? "))

#Saída de Dados
print("Apto para ingressar no clube de jogos de tabuleiro: ",(idade >= 16 and idade <= 18) and (jogo == True) and (vitoria >= 1))