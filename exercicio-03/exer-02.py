# soma de numeros positivos

soma = 0

while True:
    numero = int(input("Digite um número (ou um número negativo para encerrar): "))
    
    if numero < 0:
        break
    
    soma += numero

print(f"A soma dos números positivos digitados é: {soma}")
