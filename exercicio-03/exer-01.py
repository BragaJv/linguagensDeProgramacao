#contagem progressiva

numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    for i in range(1, numero + 1):
        print(i)
else:
    print("Por favor, digite um número inteiro positivo.")
