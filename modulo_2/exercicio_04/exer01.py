# Definindo o gerador
def contar_pares(n):
    for i in range(0, n + 1, 2):
        yield i

# Programa principal
try:
    limite = int(input("Digite um número inteiro para ver os pares até ele: "))
    print(f"\nNúmeros pares de 0 até {limite}:")
    for par in contar_pares(limite):
        print(par)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
