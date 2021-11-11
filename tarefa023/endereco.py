from dataclasses import dataclass
from bairro import Bairro
from cidade import Cidade
from estado import Estado
from logradouro import Logradouro
from pais import Pais
from tipo_endereco import TipoEndereco
from tipo_logradouro import TipoLogradouro


@dataclass
class Endereco:
    bairro: Bairro
    cidade: Cidade
    estado: Estado
    logradouro: Logradouro
    pais: Pais
    tipo_endereco: TipoEndereco
    tipo_logradouro: TipoLogradouro
    cep: int
    numero: int
    complemento_numero: str
    complemento_endereco: str
