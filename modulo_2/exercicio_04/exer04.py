try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        total_linhas = len(linhas)

        print(f"Total de linhas no arquivo: {total_linhas}\n")
        print("Conteúdo do arquivo:")
        for linha in linhas:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")
