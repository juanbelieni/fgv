"""
Estado:
    Identificador
    Quantidade

Comportamento
    Adicionar
    Remover
"""

from time import sleep
from datetime import datetime
from uuid import uuid4, UUID
from typing import Optional, List


class Livro:
    __id: UUID
    __nome: str

    __data_recebimento: datetime
    __data_doacao: Optional[datetime]

    def __init__(self, nome: str):
        self.__id = uuid4()
        self.__nome = nome

        self.__data_recebimento = datetime.now()
        self.__data_doacao = None

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def data_recebimento(self) -> datetime:
        return self.__data_recebimento

    @property
    def data_doacao(self) -> Optional[datetime]:
        return self.__data_doacao

    @property
    def foi_doado(self) -> bool:
        return self.data_doacao is not None

    def doar(self) -> None:
        if not self.foi_doado:
            self.__data_doacao = datetime.now()

    def __str__(self):
        descricao = f"{self.nome}:" \
                    f"\n  Identificador       {self.id}" \
                    f"\n  Data de recebimento {self.data_recebimento}"

        if self.foi_doado:
            descricao += f"\n  Data de doação      {self.data_doacao}"

        return descricao


class Estoque:
    __livros: List[Livro]

    def __init__(self):
        self.__livros = []

    @property
    def livros(self) -> List[Livro]:
        return self.__livros

    @property
    def quantidade_livros(self):
        return len(self.__livros)

    def receber_livro(self, novo_livro: Livro) -> None:
        self.__livros.append(novo_livro)

    def doar_livro(self, id_livro: UUID) -> None:
        for __livro in self.__livros:
            if __livro.id == id_livro:
                __livro.doar()
                break


estoque = Estoque()
livro_1984 = Livro("1984")
livro_cem_anos = Livro("Cem anos de solidão")

estoque.receber_livro(livro_1984)
estoque.receber_livro(livro_cem_anos)

print("Livros no estoque:")
for livro in estoque.livros:
    print(livro)

sleep(1)

estoque.doar_livro(livro_1984.id)

print("\nLivros no estoque:")
for livro in estoque.livros:
    print(livro)
