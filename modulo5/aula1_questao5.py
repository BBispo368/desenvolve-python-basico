import emoji

print("Emojis Disponíveis")
print(":red_heart: - ",emoji.emojize(':red_heart:'))
print(":thumbs_up: - ",emoji.emojize(':thumbs_up:'))
print(":thinking_face: - ",emoji.emojize(':thinking_face:'))
print(":partying_face: - ",emoji.emojize(':partying_face:'))

texto_novo = emoji.emojize(input("Digite uma frase e ela será emojizada: "))
print(texto_novo)
