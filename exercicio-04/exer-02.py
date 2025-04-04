
numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))


if numeros:
    maior = max(numeros)
    menor = min(numeros)
    print("Maior número da lista:", maior)
    print("Menor número da lista:", menor)
else:
    print("A lista está vazia. Digite pelo menos um número.")
