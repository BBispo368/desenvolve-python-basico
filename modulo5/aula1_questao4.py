import datetime
data = datetime.datetime.now()
data_texto = data.strftime('%d/%m/%Y')
hora_texto = data.strftime('%H:%M')

print(f"Data: {data_texto}")
print(f"Hora: {hora_texto}")
