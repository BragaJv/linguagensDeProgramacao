#classificação de idade


idade = int(input("Digite a sua idade: "))


if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
