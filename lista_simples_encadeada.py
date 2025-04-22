class Pacientes:
    def __init__(self, nome, id, estado_saude) -> None:
        self.dados = (nome, id, estado_saude)
        self.proximo = None


class ListaPacientes:
    def __init__(self):
        self.head = None

    def adicionar_paciente_head(self, nome, id, estado_saude) -> None:
        paciente = Pacientes(nome, id, estado_saude)
        paciente.proximo = self.head
        self.head = paciente

    def adicionar_paciente_tail(self, nome, id, estado_saude) -> None:
        novo_no = Pacientes(nome, id, estado_saude)

        if self.head is None:
            novo_no.proximo = self.head
            self.head = novo_no
        else:
            no_previo = self.head

            while no_previo.proximo is not None:
                no_previo = no_previo.proximo

            no_previo.proximo = novo_no
            novo_no.proximo = None

    def remover_paciente(self, id) -> None:
        no = self.head
        no_previo = None
        achou = False

        while no is not None:
            if no.dados[1] == id:
                if no_previo is None:
                    self.head = no.proximo
                else:
                    no_previo.proximo = no.proximo
                achou = True
                break
            else:
                no_previo = no
                no = no.proximo
        print("Paciente removido com sucesso!")

        if not achou:
            print("O paciente nao foi encontrado")

    def __str__(self) -> None:
        lista_nos = []
        no = self.head
        while no is not None:
            nome, id, estado_saude = no.dados
            lista_nos.append(f"[Nome: {nome}, ID: {id}, Estado de saude: {estado_saude}]")
            no = no.proximo
        lista_nos.append("None")

        return " --> ".join(lista_nos)


lista_pacientes = ListaPacientes()

lista_pacientes.adicionar_paciente_head("Joao", 1, "Em coma")

lista_pacientes.adicionar_paciente_tail("Maria", 2, "Estavel")

lista_pacientes.remover_paciente(2)

print(lista_pacientes)
