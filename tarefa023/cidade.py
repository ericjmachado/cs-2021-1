from dataclasses import dataclass


@dataclass
class Cidade:
    nome: str

    def __str__(self):
        return self.nome

    def __eq__(self, other):
        return self.nome == other.nome
