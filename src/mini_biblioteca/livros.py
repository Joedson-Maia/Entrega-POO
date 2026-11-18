class livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = str (titulo)
        self.autor = str (autor)
        self.codigo = str (codigo)
        self.status = bool (True)