def calcular_media(lista):
  
    if len(lista) == 0:
        return 0  # Evita divisão por zero caso a lista esteja vazia
    return sum(lista) / len(lista)

# Programa principal
numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
media = calcular_media(numeros)
print(f"A média dos números é: {media:.2f}")
