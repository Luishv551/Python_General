"""
2) Crie uma classe Livro que tenha os seguintes atributos:
* titulo
* autor
* ano_publicacao
E os seguintes métodos:
* detalhes: imprime o título, o autor e o ano de publicação do livro.
* e_antigo(): retorna True se o livro foi publicado antes de 2000, e False caso contrário.

"""

class Livro:
    def __init__(self, titulo, autor, ano) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def detalhes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano de Publicação: {self.ano}')
    
    def e_antigo(self):
        return self.ano < 2000

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)

livro1.detalhes()

print(livro1.e_antigo())
    