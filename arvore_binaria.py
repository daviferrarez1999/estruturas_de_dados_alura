class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade


class Node:
    def __init__(self, produto):
        self.esquerda = None
        self.direita = None
        self.produto = produto


class ArvoreProduto:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, nome, quantidade):
        novo_produto = Produto(id, nome, quantidade)
        if self.raiz is None:
            self.raiz = Node(novo_produto)
        else:
            self._inserir(novo_produto, self.raiz) 

    def _inserir(self, produto, no_atual):
        if produto.id < no_atual.produto.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = Node(produto)
            else:
                self._inserir(produto, no_atual.esquerda) 

        elif produto.id > no_atual.produto.id:
            if no_atual.direita is None:
                no_atual.direita = Node(produto)
            else:
                self._inserir(produto, no_atual.direita)

        else:
            no_atual.produto.nome = produto.nome
            no_atual.produto.quantidade = produto.quantidade

    def buscar(self, id):
        return self._buscar(id, self.raiz)
   
    def _buscar(self, id, no_atual):
        if no_atual is None:
            return None
        if id == no_atual.produto.id:
            return no_atual
        elif id < no_atual.produto.id:
            return self._buscar(id, no_atual.esquerda)
        else:
            return self._buscar(id, no_atual.direita)
   

produtos = ArvoreProduto()

produtos.inserir(1, "Refrigerante", 20)
produtos.inserir(2, "Sabao em po", 15)

busca = produtos.buscar(3)
if busca:
    print(f"Produto encontrado: {busca.produto.nome}, Quantidade: {busca.produto.quantidade}")
else:
    print("O produto nao foi encontrado")
