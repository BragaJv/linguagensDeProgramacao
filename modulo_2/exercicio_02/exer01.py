
frase = input("Digite uma frase: ").lower()  
vogais = 'aeiou'
contagem_vogais = {vogal: frase.count(vogal) for vogal in vogais}

print("\nQuantidade de vogais na frase:")
for vogal, quantidade in contagem_vogais.items():
    print(f"{vogal}: {quantidade}")

# Frase ao contrário
frase_invertida = frase[::-1]
print("\nFrase ao contrário:")
print(frase_invertida)

# Substituir espaços por hífens
frase_com_hifen = frase.replace(" ", "-")
print("\nFrase com espaços substituídos por '-':")
print(frase_com_hifen)
