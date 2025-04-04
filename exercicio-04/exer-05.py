
numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))


alvo = int(input("Digite o número que deseja contar: "))

ocorrencias = numeros.count(alvo)


print(f"O número {alvo} aparece {ocorrencias} vez(es) na lista.")
