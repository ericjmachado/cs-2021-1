from abc import ABCMeta, abstractmethod
from typing import List
from bairro import Bairro
from cidade import Cidade
from endereco import Endereco
from estado import Estado
from logradouro import Logradouro
from pais import Pais
from tipo_endereco import TipoEndereco
from tipo_logradouro import TipoLogradouro


class EnderecoService(metaclass=ABCMeta):

    def __init__(self, enderecos: List[Endereco] = []):
        self.enderecos = enderecos

    @abstractmethod
    def consulta_por_tipo_logradouro(self, tipo_logradouro: TipoLogradouro) -> List[Logradouro]:
        pass

    @abstractmethod
    def consulta_por_tipo_endereco(self, tipo_endereco: TipoEndereco) -> List[Endereco]:
        pass

    @abstractmethod
    def consulta_por_cep(self, cep: int) -> List[Endereco]:
        pass

    @abstractmethod
    def consulta_por_logradouro(self, logradouro: Logradouro) -> List[Endereco]:
        pass


    @abstractmethod
    def consulta_por_bairro(self, bairro: Bairro) -> List[Endereco]:
        pass

    @abstractmethod
    def consulta_por_cidade(self, cidade: Cidade) -> List[Endereco]:
        pass


    @abstractmethod
    def lista_cidades_por_estados(self, estado: Estado) -> List[Cidade]:
        pass


    @abstractmethod
    def consulta_por_pais(self, pais: Pais) -> List[Estado]:
        pass
