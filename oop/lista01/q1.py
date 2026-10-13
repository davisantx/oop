class Livro:
    def __init__(self, nome, autor, genero, ano):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.ano = ano


dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", "romance", 1899)
o_hobbit = Livro("O Hobbit", "J.R.R. Tolkien", "fantasia", 1937)

print(f"{dom_casmurro.autor}: {dom_casmurro.nome} ({dom_casmurro.ano})")
print(f"O gênero do livro {o_hobbit.nome} é {o_hobbit.genero}")