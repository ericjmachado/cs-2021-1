import traceback


class ContatoNaoEncontratoException(Exception):
    pass


class Contato:
    def __init__(self, nome: str, telefone=None, email=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return self.nome


class Agenda:
    def __init__(self, contatos=None):
        if not contatos:
            contatos = list()
        self.contatos: list[Contato] = contatos

    def remover(self, contato: Contato):
        self.contatos.remove(contato)

    def remover_todos(self):
        self.contatos = list()

    def adicionar(self, contato: Contato):
        self.contatos.append(contato)

    def buscar(self, nome: str):
        contato_encontrado = None
        for contato in self.contatos:
            if contato.nome == nome:
                contato_encontrado = contato
                break
        if contato_encontrado:
            print(str(contato_encontrado))
        else:
            raise ContatoNaoEncontratoException("Contato não encontrado")


class AgendaTeste:
    def __init__(self):
        agenda = Agenda()
        agenda.adicionar(Contato("Contato 1", "111-111", "email2@email.com"))
        agenda.adicionar(Contato("Contato 2", "222-222", "email3@email.com"))
        agenda.adicionar(Contato("Contato 3", "333-333", "email4@email.com"))

        try:
            agenda.buscar("Contato 4")
        except ContatoNaoEncontratoException as e:
            print("Contato não encontrado!")
            print("\033[91m" + traceback.format_exc())
        finally:
            agenda.remover_todos()


if __name__ == "__main__":
    AgendaTeste()
