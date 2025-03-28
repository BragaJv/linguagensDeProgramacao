def pedir_numero():
    while True:
        try:
           
            numero = int(input("Digite um número inteiro: "))
           
            print(f"O dobro de {numero} é {numero * 2}.")
            break  
        except ValueError:
          
            print("Erro: Por favor, digite um número inteiro válido.")


pedir_numero()
