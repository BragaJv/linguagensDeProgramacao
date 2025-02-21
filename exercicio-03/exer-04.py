#numeros impares em um intervalo

A = int(input("Digite o primeiro número (A): "))
B = int(input("Digite o segundo número (B): "))


if A > B:
    A, B = B, A

print(f"Números ímpares no intervalo de {A} a {B}:")

for num in range(A, B + 1):
    if num % 2 != 0:
        print(num)
