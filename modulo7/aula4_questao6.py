# Importando a biblioteca csv
import csv

# Criando uma lista para armazenar as músicas mais populares de cada ano
top_songs = []

# Abrindo o arquivo CSV para leitura
with open('spotify-2023.csv', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile)
    # Lendo cada linha do arquivo
    for row in reader:
        # Verificando se a música foi lançada entre 2012 e 2022
        if isinstance(row[3], int):
        # Se o valor for um inteiro, você pode continuar com a sua lógica
            if int(row[3]) >= 2012 and int(row[3]) <= 2022:
            # Verificando se a música não está entre aspas
                if '"' not in row[0]:
                # Adicionando a música à lista top_songs
                    top_songs.append([row[0], row[1], int(row[3]), int(row[8])])

# Criando uma lista para armazenar as músicas mais populares de cada ano
top_songs_by_year = []

# Iterando sobre os anos de 2012 a 2022
for year in range(2012, 2023):
    # Criando uma lista para armazenar as músicas do ano atual
    songs_this_year = []

    # Iterando sobre as músicas na lista top_songs
    for song in top_songs:
        # Verificando se a música foi lançada no ano atual
        if song[2] == year:
            # Adicionando a música à lista songs_this_year
            songs_this_year.append(song)

    # Ordenando a lista songs_this_year pelo número de streams
    songs_this_year.sort(key=lambda x: x[3], reverse=True)

    # Adicionando a música mais popular do ano à lista top_songs_by_year
    if len(songs_this_year) > 0:
        top_songs_by_year.append(songs_this_year[0])

# Imprimindo a lista top_songs_by_year
print(top_songs_by_year)