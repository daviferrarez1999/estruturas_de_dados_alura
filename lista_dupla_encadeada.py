class Produto:
    def __init__(self, nome, codigo, preco, qtd_estoque) -> None:
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.quantidade = 0

    def adicionar_produto_head(self, nome, codigo, preco, qtd_estoque) -> None:
        novo_no = Produto(nome, codigo, preco, qtd_estoque)
        
        novo_no.proximo = self.head
        novo_no.anterior = None

        if self.head is not None:
            self.head.anterior = novo_no
        else:
            self.tail = novo_no
        
        self.head = novo_no
        self.quantidade += 1

    def adicionar_produto_tail(self, nome, codigo, preco, qtd_estoque) -> None:
        novo_no = Produto(nome, codigo, preco, qtd_estoque)

        novo_no.proximo = None
        novo_no.anterior = self.tail

        if self.tail is not None:
            self.tail.proximo = novo_no
        else:
            self.head = novo_no

        self.tail = novo_no
        self.quantidade += 1

    def atualizar_estoque(self, codigo, nova_qtd_estoque) -> None:
        no = self.head

        while no is not None:
            if no.codigo == codigo:
                no.qtd_estoque = nova_qtd_estoque
                print(f"Estoque atualizado com sucesso! Novo estoque de {no.nome}: {no.qtd_estoque}")
                return
            no = no.proximo

    def buscar_produto(self, codigo) -> None:
        no = self.head

        while no is not None:
            if no.codigo == codigo:
                print(f"O produto foi encontrado: [Nome: {no.nome}, Codigo: {no.codigo}, Preco: R$ {no.preco:.2f}, Quantidade em estoque: {no.qtd_estoque}]")
                return
            no = no.proximo

        print("Produto nao encontrado")

    def remover_produto(self, codigo) -> None:
        no = self.head

        while no is not None:
            if no.codigo == codigo:
                if no.anterior is not None:
                    no.anterior.proximo = no.proximo
                else:
                    self.head = no.proximo

                if no.proximo is not None:
                    no.proximo.anterior = no.anterior
                else:
                    self.tail = no.anterior
             
                self.quantidade -= 1
                print(f"{no.nome} removido com sucesso!")         
                return
  
            no = no.proximo

        print("O produto nao foi encontrado")

    def __str__(self) -> str:
        lista_nos = []
        no = self.head
        while no is not None:
            lista_nos.append(f"[Nome: {no.nome}, Codigo: {no.codigo}, Preco: {no.preco}, Quantidade em estoque: {no.qtd_estoque}]")
            no = no.proximo
        lista_nos.append("None")

        return " --> ".join(lista_nos)


lista_produtos = ListaDuplamenteEncadeada()

lista_produtos.adicionar_produto_head("Arroz", 1, 15.00, 20)

lista_produtos.adicionar_produto_tail("Feijao", 2, 10.00, 30)

lista_produtos.atualizar_estoque(1, 25)

lista_produtos.buscar_produto(2)

lista_produtos.remover_produto(1)

print(lista_produtos)
