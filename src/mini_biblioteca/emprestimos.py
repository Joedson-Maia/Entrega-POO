from .usuarios import usuario , id_usuario
from .livros import titulo , autor , codigo , disponivel

class emprestimo:
    def __init__(self, usuario, titulo):
        self.usuario = usuario
        self.id_usuario = usuario
        self.titulo = titulo
        self.disponivel = True
        self.ativo = True

def devolver(self, livro):
    livro.status = livro
    emprestimo.ativo = False
    return True

@property
def livro_emprestimo(self):
    return livro_emprestimo

@emprestimo.ativo.setter
def validar_emprestimo(self, status_ativo):
    if status_ativo == True:
        raise ValueError(f"{titulo} não está disponivel para emprestimos")


