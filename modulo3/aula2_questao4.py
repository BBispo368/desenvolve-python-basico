#Leitura de Dados
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

#Saída de Dados
print("Pontos de atributo consistentes com a classe escolhida: ", ((classe == "guerreiro") and (forca >= 15) and (magia <= 10)) or ((classe == "mago") and (forca <= 10) and (magia >= 15)) or ((classe == "arqueiro") and (forca > 5 and forca < 15) and (magia > 5 and magia < 15)))