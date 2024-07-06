frase = input("Digite uma frase: ")
palavra = input("Digite a palavra objetivo: ")
lista = [frase[i:i+len(palavra)] for i in range(len(frase) - len(palavra)) if sorted(frase[i:i+len(palavra)]) == sorted(palavra)]
print(lista)