import os
with open('frase.txt','r') as f:
    frase = f.read()

palavras = frase.split()
print(palavras)
with open('palavras.txt','w') as f:
    for palavra in palavras:
        f.write(palavra+'\n')
with open('palavras.txt','r') as f:
    print(f.read())