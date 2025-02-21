#Calculo de média e aprovação


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


if media >= 7:
    print(f"Média: {media:.2f} - Aluno APROVADO!")
elif 5 <= media < 7:
    print(f"Média: {media:.2f} - Aluno em RECUPERAÇÃO!")
else:
    print(f"Média: {media:.2f} - Aluno REPROVADO!")

