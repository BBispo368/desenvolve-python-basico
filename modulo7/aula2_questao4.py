
def validador_senha(senha):
    if len(senha) < 8: return False
    teste_minusculo = 0
    teste_maiusculo = 0
    teste_numero = 0
    teste_especial = 0
    for i in range(len(senha)):
        if senha[i].islower():
            teste_minusculo = 1
            continue
        elif senha[i].isupper():
            teste_maiusculo = 1
            continue
        elif senha[i].isdecimal():
            teste_numero = 1
            continue
        else:
            teste_especial =1
    if teste_maiusculo + teste_minusculo + teste_numero + teste_especial == 4: return True
    else: return False

print(validador_senha("Mariadoce@1"))