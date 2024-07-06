import random
def encrypt(nomes):
    nomes_cript = []
    chave = random.randint(0,10)
    for i in range(len(nomes)):
        sub_nomes = [chr(ord(nomes[i][j]) + chave) if (ord(nomes[i][j]) + chave) <= 126 else chr(126)  for j in range(len(nomes[i]))]
        nomes_cript.append(''.join(sub_nomes))
    return nomes_cript,chave
