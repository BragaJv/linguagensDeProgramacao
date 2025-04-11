try:
    # Solicita os números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Tenta fazer a divisão
    resultado = num1 / num2
    print(f"\nResultado da divisão: {resultado:.2f}")

except ZeroDivisionError:
    print("\nErro: Não é possível dividir por zero.")

except ValueError:
    print("\nErro: Por favor, digite apenas números válidos.")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")
