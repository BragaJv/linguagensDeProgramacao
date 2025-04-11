import math
import random


numero = float(input("Digite um número para calcular a raiz quadrada: "))

raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")


numero_aleatorio = random.randint(1, 100)
print(f"Número aleatório gerado entre 1 e 100: {numero_aleatorio}")
