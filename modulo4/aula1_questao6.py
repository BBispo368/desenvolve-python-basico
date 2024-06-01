qtd_exp = int(input())
cont = 0

total_cobaia = 0
total_coelho = 0
total_rato = 0
total_sapo = 0

while cont < qtd_exp:

    qtd_cobaia = int(input())
    cobaia = input()

    if cobaia == 'C':
        total_coelho += qtd_cobaia

    elif cobaia == 'R':
        total_rato += qtd_cobaia

    else:
        total_sapo += qtd_cobaia
    
    total_cobaia+=qtd_cobaia

    cont+=1

print(f"Total: {total_cobaia} cobaias")
print("Total de coelhos: ",total_coelho)
print("Total de ratos: ",total_rato)
print("Total de sappos: ",total_sapo)
print(f"Percentual de coelhos: {(total_coelho*100)/total_cobaia:.2f}%")
print(f"Percentual de ratos: {(total_rato*100)/total_cobaia:.2f}%")
print(f"Percentual de sapos: {(total_sapo*100)/total_cobaia:.2f}%")