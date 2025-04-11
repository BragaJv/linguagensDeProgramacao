# Classe base
class Animal:
    def fazer_som(self):
        print("O animal faz um som.")

# Subclasse Cachorro
class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late: Au au!")

# Subclasse Gato
class Gato(Animal):
    def fazer_som(self):
        print("O gato mia: Miau!")

# Programa principal
animal_generico = Animal()
cachorro = Cachorro()
gato = Gato()

animal_generico.fazer_som()
cachorro.fazer_som()
gato.fazer_som()
