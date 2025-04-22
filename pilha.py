class Livro:
    def __init__(self, titulo, num_paginas):
        self.titulo = titulo
        self.num_paginas = num_paginas

    def __str__(self):
        return f"[Titulo do livro: {self.titulo}, Numero de paginas: {self.num_paginas}]"


class PilhaDeLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, num_paginas):
        novo_livro = Livro(titulo, num_paginas)
        self.livros.append(novo_livro)

    def pilha_vazia(self):
        return len(self.livros) == 0

    def remover_livro(self):
        if self.pilha_vazia():
            return None
        else:
            self.livros.pop()
        
    def exibir_todos_livros(self):
        if self.pilha_vazia():
            return "Nao ha livros para serem exibidos"
        
        return " , ".join(str(livro) for livro in self.livros)
  
    def __str__(self):
        return self.exibir_todos_livros()
   
    def exibir_livro_topo(self):
        if self.pilha_vazia():
            return None
     
        return self.livros[-1]


pilha_livros = PilhaDeLivros()

pilha_livros.adicionar_livro("A Game of Thrones", 704)
pilha_livros.adicionar_livro("A Clash of Kings", 784)
pilha_livros.adicionar_livro("A Storm of Swords", 992)
pilha_livros.adicionar_livro("A Feast for Crows", 784)
pilha_livros.adicionar_livro("A Dance with Dragons", 959)

pilha_livros.remover_livro()

print(pilha_livros)

print(f"Topo da pilha: {pilha_livros.exibir_livro_topo()}")
