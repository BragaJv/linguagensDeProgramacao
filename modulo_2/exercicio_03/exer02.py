# Definindo a classe Livro
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} - {self.paginas} páginas"

    def __len__(self):
        return self.paginas

# Programa principal
livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)

# Exibindo os detalhes com __str__()
print(livro1)

# Exibindo o número de páginas com __len__()
print(f"Número de páginas: {len(livro1)}")
