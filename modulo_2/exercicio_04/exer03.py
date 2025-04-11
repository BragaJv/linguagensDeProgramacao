# Definindo a closure
def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

# Programa principal
dobro = multiplicador(2)
triplo = multiplicador(3)

print("Testando closures:")
print(f"Dobro de 5: {dobro(5)}")
print(f"Triplo de 7: {triplo(7)}")
