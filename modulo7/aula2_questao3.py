menu = 0
while menu == 0:
    frase = input("Digite a frase: ")
    if frase.lower() == "fim":
        break
    
    frase_lista = [frase[i] for i in range(len(frase)) if frase[i].isalpha()]
    frase_analise = ''.join(frase_lista)

    if frase_analise.lower() == frase_analise[::-1].lower():
        print("Palindromo")
    else:print("Não é palindromo")