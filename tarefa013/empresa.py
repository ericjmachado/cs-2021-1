class Cargo:
    def __init__(self, comissao: float):
        self.comissao = comissao


class Gerente(Cargo):
    def __init__(self):
        super(Gerente, self).__init__(1500)


class Supervisor(Cargo):
    def __init__(self):
        super(Supervisor, self).__init__(600)


class Vendedor(Cargo):
    def __init__(self):
        super(Vendedor, self).__init__(250)


class Funcionario:
    def __init__(self, nome: str, codigo: str, cargo: Cargo = None):
        self.nome = nome
        self.codigo = codigo
        self.renda_base = 1000
        self.cargo = cargo

    @property
    def salario(self):
        bonus = 0
        if self.cargo is not None:
            bonus = self.cargo.comissao
        return self.renda_base + bonus

    def __str__(self):
        return f"Funcionario {self.nome}, comissao: {self.cargo.comissao if self.cargo is not None else 0}, salario: ${self.salario} "


class FuncionarioBasico(Funcionario):
    def __init__(self, escola: str, *args, **kwargs):
        super(FuncionarioBasico, self).__init__(*args, **kwargs)
        self.escola = escola
        self.renda_base = self.renda_base + self.renda_base * 0.1


class FuncionarioMedio(FuncionarioBasico):
    def __init__(self, *args, **kwargs):
        super(FuncionarioMedio, self).__init__(*args, **kwargs)
        self.renda_base = self.renda_base + self.renda_base * 0.5


class FuncionarioSuperior(FuncionarioMedio):
    def __init__(self, universidade: str, graduacao: str, *args, **kwargs):
        super(FuncionarioSuperior, self).__init__(*args, **kwargs)
        self.universidade = universidade
        self.graduacao = graduacao
        self.renda_base = self.renda_base * 2


def programa():
    empresa = list()
    gerente = Gerente()
    supervisor = Supervisor()
    vendedor = Vendedor()

    empresa.append(FuncionarioBasico("Federal", "Romario", "1212", vendedor))
    empresa.append(FuncionarioBasico("Municipal", "Luiz", "1340", vendedor))
    empresa.append(FuncionarioBasico("Municipal", "Yan", "5427", supervisor))
    empresa.append(FuncionarioBasico("Municipal", "Mateus", "45545", vendedor))

    empresa.append(FuncionarioMedio("Federal", "Julia", "5387", vendedor))
    empresa.append(FuncionarioMedio("Municipal", "Roberto", "52287", gerente))
    empresa.append(FuncionarioMedio("Municipal", "Eric", "1211", gerente))
    empresa.append(FuncionarioMedio("Municipal", "Weverton", "3121", gerente))

    empresa.append(FuncionarioSuperior("UFG", "CC", "Estadual", "Leandro", "1212", gerente))
    empresa.append(FuncionarioSuperior("UFG", "CC", "Municipal", "Roberto", "587", supervisor))

    print(f"A empresa gasta por mês {sum(funcionario.salario for funcionario in empresa)}")

    for funcionario in empresa:
        print(str(funcionario))
