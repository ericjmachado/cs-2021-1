from typing import List

from bairro import Bairro
from cidade import Cidade
from endereco import Endereco
from endereco_service import EnderecoService
from estado import Estado
from logradouro import Logradouro
from pais import Pais
from tipo_endereco import TipoEndereco
from tipo_logradouro import TipoLogradouro


class CadastroEndereco(EnderecoService):
    def __init__(
        self,
        tipo_endereco: str,
        tipo_logradouro: str,
        logradouro: str,
        numero: int,
        complemento_numero: str,
        complemento_endereco: str,
        bairro: str,
        cep: int,
        cidade: str,
        pais: str,
        estado: str,
    ):
        super(CadastroEndereco, self).__init__()
        self.tipo_logradouro = TipoLogradouro(tipo_logradouro)
        self.logradouro = Logradouro(logradouro)
        self.bairro = Bairro(bairro)
        self.cidade = Cidade(cidade)
        self.estado = Estado(estado)
        self.pais = Pais(pais)
        self.tipo_endereco = TipoEndereco(tipo_endereco)
        self.endereco = Endereco(
            self.bairro,
            self.cidade,
            self.estado,
            self.logradouro,
            self.pais,
            self.tipo_endereco,
            self.tipo_logradouro,
            cep,
            numero,
            complemento_numero,
            complemento_endereco,
        )
        self.enderecos.append(self.endereco)

    def consulta_por_tipo_endereco(self, tipo_endereco: TipoEndereco) -> List[Endereco]:
        return list(
            filter(
                lambda endereco: endereco.tipo_endereco == tipo_endereco, self.enderecos
            )
        )

    def consulta_por_tipo_logradouro(
        self, tipo_logradouro: TipoLogradouro
    ) -> List[Endereco]:
        return list(
            filter(
                lambda endereco: endereco.tipo_logradouro == tipo_logradouro,
                self.enderecos,
            )
        )

    def consulta_por_cep(self, cep: int) -> List[Endereco]:
        return list(filter(lambda endereco: endereco.cep == cep, self.enderecos))

    def consulta_por_logradouro(self, logradouro: Logradouro) -> List[Endereco]:
        return list(
            filter(lambda endereco: endereco.logradouro == logradouro, self.enderecos)
        )

    def consulta_por_bairro(self, bairro: Bairro) -> List[Endereco]:
        return list(filter(lambda endereco: endereco.bairro == bairro, self.enderecos))

    def consulta_por_cidade(self, cidade: Cidade) -> List[Endereco]:
        return list(filter(lambda endereco: endereco.cidade == cidade, self.enderecos))

    def lista_cidades_por_estados(self, estado: Estado) -> List[Cidade]:
        return [
            endereco.cidade
            for endereco in list(
                filter(lambda endereco: endereco.estado == estado, self.enderecos)
            )
        ]

    def consulta_por_pais(self, pais: Pais) -> List[Estado]:
        return [
            endereco.estado
            for endereco in list(
                filter(lambda endereco: endereco.pais == pais, self.enderecos)
            )
        ]
