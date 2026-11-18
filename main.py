from src.mini_biblioteca import usuario, livro, emprestimo

usu_1 = usuario("João","5555")
livro_1 = livro("Assis", "Machado", "6666")

emprestimo1 = emprestimo(usu_1, livro_1)
print(usu_1)
print(emprestimo1)