class ListaDeCompras:
    def __init__(self):
        self.itens = []
        self.quantidades = []

    def adicionar_item(self, item, quantidade):
        self.itens.append(item)
        self.quantidades.append(quantidade)

    def remover_itens(self, nome):
        if nome in self.itens:
            indice_produto = self.itens.index(nome)
            self.itens.pop(indice_produto)
            self.quantidades.pop(indice_produto)
            print(f"{nome} removido da lista")
        else:
            print(f"{nome} nao esta na lista")

    def listar_itens(self):
        for i in range(len(self.itens)):
            print(f"[{self.itens[i]}: {self.quantidades[i]}]")


lista = ListaDeCompras()

lista.adicionar_item("Arroz", 5)
lista.adicionar_item("Feijao", 5)

lista.remover_itens("Arroz")

lista.listar_itens()
