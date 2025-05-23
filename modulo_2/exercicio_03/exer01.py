# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-" * 30)

# Programa principal
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Ford", "Mustang", 2022)

print("Detalhes do Carro 1:")
carro1.exibir_detalhes()

print("Detalhes do Carro 2:")
carro2.exibir_detalhes()
