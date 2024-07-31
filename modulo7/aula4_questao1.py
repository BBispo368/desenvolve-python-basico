import os
frase = input("Digite uma frase: ")
with open('frase.txt','w') as f:
    f.write(frase)
print('frase salva em ',os.path.abspath('frase.txt'))