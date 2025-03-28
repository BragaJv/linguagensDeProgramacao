def ler_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")
    
    try:
       
        with open(nome_arquivo, 'r') as arquivo:
            
            conteudo = arquivo.read()
            print("\nConteúdo do arquivo:")
            print(conteudo)
    
    except FileNotFoundError:
       
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError:
        
        print(f"Erro: Não foi possível ler o arquivo '{nome_arquivo}'.")
    except Exception as e:
        
        print(f"Ocorreu um erro inesperado: {e}")


ler_arquivo()
