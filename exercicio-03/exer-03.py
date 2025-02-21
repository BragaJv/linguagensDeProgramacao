#tabuada de um numero

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break  # Se a conversão for bem-sucedida, sai do loop
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
