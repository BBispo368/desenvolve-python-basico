data = input("Digite uma data de nascimento: ")
dia = data[:2]
mes = data[3:5]
mes_lista = ["Janeiro", "Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
mes_extenso = mes_lista[int(mes)-1]
ano = data[6:]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")