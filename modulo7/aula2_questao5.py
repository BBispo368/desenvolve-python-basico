import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_modificadas = []
    for palavra in palavras:
        if len(palavra) > 3:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])
            random.shuffle(letras_internas)
            palavra_modificada = primeira_letra + ''.join(letras_internas) + ultima_letra
        else:
            palavra_modificada = palavra
        palavras_modificadas.append(palavra_modificada)
    frase_modificada = ' '.join(palavras_modificadas)
    return frase_modificada
frase = "Quero ver conseguir ler um textão igual a esse, que é bem complicado de inicio, porem pode ser que der certo ne, vamos ver"
print(embaralhar_palavras(frase))