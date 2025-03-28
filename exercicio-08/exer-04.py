numeros = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um índice (0 a 4): "))
    print(f"Valor no índice {indice}: {numeros[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo válido (0 a 4).")
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
