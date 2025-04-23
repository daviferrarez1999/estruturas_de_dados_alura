class Jogo:
    def __init__(self):
        self.jogadores = []

    def adicionar_jogadores(self, nome, pontos):
        jogador = {'nome_jogador': nome, 'num_pontos': pontos}
        self.jogadores.append(jogador)

    def atualizar_pontuacoes(self, nome, nova_pontuacao):
        for jogador in self.jogadores:
            if jogador['nome_jogador'] == nome:
                jogador['num_pontos'] = nova_pontuacao
                return f"Nova pontuacao de {nome}: {nova_pontuacao}"
        return f"O jogador {nome} nao foi encontrado."
   
    def remover_jogadores(self, nome):
        for jogador in self.jogadores:
            if jogador['nome_jogador'] == nome:
                self.jogadores.remove(jogador)
                return f"O jogador {nome} foi removido com sucesso!"
        return f"O jogador {nome} nao foi encontrado."
    
    def listar_jogadores_ordem_decrescente(self):
        ordem_descrescente = sorted(self.jogadores, key=lambda j: j['num_pontos'], reverse=True)
        resultado = [f"{j['nome_jogador']}: {j['num_pontos']} pontos" for j in ordem_descrescente]
        return "\n".join(resultado)

    def jogador_vencedor(self):
        if not self.jogadores:
            return "Nao existem jogadores cadastrados"
        
        vencedor = max(self.jogadores, key=lambda j: j['num_pontos'])

        return f"Vencedor: {vencedor['nome_jogador']} com {vencedor['num_pontos']} pontos!"
                       

novo_jogo = Jogo()

novo_jogo.adicionar_jogadores('Davi', 9)
novo_jogo.adicionar_jogadores('Joao', 10)
novo_jogo.adicionar_jogadores("Maria", 5)

print(novo_jogo.atualizar_pontuacoes("Davi", 20))

print(novo_jogo.remover_jogadores("Joao"))

print(novo_jogo.listar_jogadores_ordem_decrescente())

print(novo_jogo.jogador_vencedor())
