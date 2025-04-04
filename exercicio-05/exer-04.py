def contar_vogais(palavra):
    """Retorna a quantidade de vogais na palavra."""
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in palavra if letra in vogais)
    return contador

# Programa principal
palavra = input("Digite uma palavra: ")
quantidade_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' contém {quantidade_vogais} vogal(is).")
