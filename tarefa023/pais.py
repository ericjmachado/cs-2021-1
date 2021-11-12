from dataclasses import dataclass


@dataclass
class Pais:
    nome: str

    def __str__(self):
        return self.nome

    def __eq__(self, other):
        return self.nome == other.nome
