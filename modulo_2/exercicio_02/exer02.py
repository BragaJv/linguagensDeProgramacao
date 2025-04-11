# Solicita uma lista de palavras separadas por espaço
entrada = input("Digite uma lista de palavras separadas por espaço: ")

# Divide a string em uma lista
palavras = entrada.split()

# Ordena a lista
palavras_ordenadas = sorted(palavras)

# Conta o número total de palavras
total_palavras = len(palavras)

# Converte as palavras para maiúsculas
palavras_maiusculas = [palavra.upper() for palavra in palavras]

# Exibe os resultados
print("\nLista ordenada alfabeticamente:")
print(palavras_ordenadas)

print(f"\nNúmero total de palavras: {total_palavras}")

print("\nPalavras em maiúsculas:")
print(palavras_maiusculas)
