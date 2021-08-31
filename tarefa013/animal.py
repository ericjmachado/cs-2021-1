from abc import ABC


class Animal(ABC):
    def __init__(self, som: str, acao: str, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.som = som
        self.acao = acao

    def emitir_som(self):
        print(self.som)

    def agir(self):
        print(self.acao)


class Cachorro(Animal):
    def __init__(self, *args, **kwargs):
        super(Cachorro, self).__init__(*args, **kwargs, som="latir", acao="Correr")


class Cavalo(Animal):
    def __init__(self, *args, **kwargs):
        super(Cavalo, self).__init__(*args, **kwargs, som="relinchar", acao="Correr")


class Preguica(Animal):
    def __init__(self, *args, **kwargs):
        super(Preguica, self).__init__(
            *args, **kwargs, som="Som de preguica", acao="Subir em árvores"
        )


class AnimalTeste:
    def __init__(self):
        cachorro = Cachorro()
        cavalo = Cavalo()
        preguica = Preguica()

        cachorro.emitir_som()
        cavalo.emitir_som()
        preguica.emitir_som()


class Veterinario:
    def __init__(self, animal: Animal):
        self.animal = animal

    def examinar(self):
        self.animal.emitir_som()


class Zoologico:
    def __init__(self, animais: list[Animal]):
        self.animais = animais

        for animal in animais:
            animal.emitir_som()
            animal.agir()
