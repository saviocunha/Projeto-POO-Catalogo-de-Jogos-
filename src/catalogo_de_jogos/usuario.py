from colecao import Colecao

from jogo import Jogo

class Usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__catalogo = Colecao('Catálogo Principal')
        self.__colecoes = []


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome == '':
            raise ValueError('O nome do usuário não pode ser vazio.')
        self.__nome = nome

    @property
    def catalogo(self):
        return self.__catalogo

    @property
    def colecoes(self):
        return self.__colecoes.copy()

    # Operações

    def adicionar_jogo(self, jogo: Jogo):
        self.__catalogo.adicionar_jogo(jogo)

    def remover_jogo(self, jogo: Jogo):
        self.__catalogo.remover_jogo(jogo)


    def tempo_total_jogado(self):
        return self.__catalogo.total_horas()


    def __str__(self):
        return(f'Usuário {self.nome} | Qnt de jogos: {len(self.catalogo.jogos)}')
