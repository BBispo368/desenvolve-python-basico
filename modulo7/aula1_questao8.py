def multisoma(lista_cpf, multiplicador):
    soma = 0
    for i in range(len(lista_cpf)):
        soma += lista_cpf[i]*multiplicador[i]
    if soma % 11 < 2:
        return 0
    else:
        return 11 - soma % 11
    
cpf = input("Digite seu CPF: ")
int_cpf = [int(cpf[i]) for i in range(len(cpf)) if ord(cpf[i]) >= 48 and ord(cpf[i]) <= 57]

multiplicador1 = [i for i in range(10,1,-1)]
primeiro_digito = multisoma(int_cpf[:9],multiplicador1)

if primeiro_digito != int_cpf[9]:
    print("CPF Inválido")
else:
    multiplicador2 = [i for i in range(11,1,-1)]
    segundo_digito = multisoma(int_cpf[:10],multiplicador2)
    if segundo_digito != int_cpf[10]:
        print("CPF Inválido")
    else:
        print("CPF Válido")