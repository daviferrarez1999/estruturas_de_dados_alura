class Pedido:
    def __init__(self, num_pedido, nome_cliente, itens_pedido, valor_total):
        self.num_pedido = num_pedido
        self.nome_cliente = nome_cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total

    def __str__(self):
        return (f"[Numero do pedido: {self.num_pedido}, Nome do cliente: {self.nome_cliente}, Itens do pedido: {self.itens_pedido}, Valor total: R$ {self.valor_total:.2f}]")


class FilaDePedidos:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, num_pedido, nome_cliente, itens_pedido, valor_total):
        novo_pedido = Pedido(num_pedido, nome_cliente, itens_pedido, valor_total)
        self.pedidos.append(novo_pedido)

    def fila_vazia(self):
        return len(self.pedidos) == 0

    def remover_pedido(self):
        if self.fila_vazia():
            return None
        else:
            self.pedidos.pop(0)

    def listar_pedidos(self):
        if self.fila_vazia():
            return "Nenhum pedido na fila."

        return " , ".join(str(pedido) for pedido in self.pedidos)

    def __str__(self):
        return self.listar_pedidos()


fila_pedidos = FilaDePedidos()

fila_pedidos.adicionar_pedido(1, "Davi", "Arroz, strogonoff de frango, batata palha", 30.00)
fila_pedidos.adicionar_pedido(2, "Joao", "Pizza de Calabresa", 45.00)

fila_pedidos.remover_pedido()

print(fila_pedidos)
