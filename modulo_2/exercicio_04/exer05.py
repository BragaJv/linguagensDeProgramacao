import pickle

# Lista de números inteiros para gravar
numeros = [10, 20, 30, 40, 50]

# Gravando a lista no arquivo binário
with open("dados.bin", "wb") as arquivo:
    pickle.dump(numeros, arquivo)

print("Números gravados com sucesso no arquivo 'dados.bin'.\n")

# Lendo e exibindo os números do arquivo
with open("dados.bin", "rb") as arquivo:
    numeros_lidos = pickle.load(arquivo)

print("Números lidos do arquivo:")
print(numeros_lidos)
