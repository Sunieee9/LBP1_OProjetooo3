class Livro:
    def __init__(self, id, titulo , preco):
        self.id = id
        self.titulo = titulo
        self.preco = preco

Livrinhos = [
    Livro(1, 'Harry Potter', 500),
    Livro(2, 'Crepúsculo', 30),
    Livro(3, 'Cruella', 200)
]