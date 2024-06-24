def vogal(vogal):
    if vogal == ' ':
        return
    elif vogal =='a' or vogal =='A' or vogal =='e' or vogal =='E' or vogal =='i' or vogal =='I' or vogal =='o' or vogal =='O' or vogal =='u' or vogal =='U':
        return True
    else: return False

frase = input("Escreva a frase: ")

vogais = [i for i in frase if vogal(i) == True]
print(sorted(vogais))

consoantes = [i for i in frase if vogal(i) == False]
print(consoantes)