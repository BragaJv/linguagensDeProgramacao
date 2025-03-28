class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Erro: Saldo insuficiente para o saque."):
        super().__init__(mensagem)

saldo = 1000.00

try:
    saque = float(input("Digite o valor para saque: "))
    if saque > saldo:
        raise SaldoInsuficienteError()
    saldo -= saque
    print(f"Saque realizado com sucesso! Saldo restante: R$ {saldo:.2f}")
except SaldoInsuficienteError as e:
    print(e)
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido.")
