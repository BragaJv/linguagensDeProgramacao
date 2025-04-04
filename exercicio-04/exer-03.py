
numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))


sem_duplicatas = []
for num in numeros:
    if num not in sem_duplicatas:
        sem_duplicatas.append(num)

print("Lista sem duplicatas:", sem_duplicatas)
