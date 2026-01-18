from .colecao import Colecao

from catalogo_de_jogos.jogo import Jogo

class Usuario:
    def __init__(self, nome):
        """Inicializa um novo usuário."""
        self.nome = nome
        self.__catalogo = Colecao('Catálogo Principal')
        self.__colecoes = []


    @property
    def nome(self):
        """Retorna o nome do usuário."""
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """Define o nome do usuário com validação."""
        if nome == None or nome.strip() == '':
            raise ValueError('O nome do usuário não pode ser vazio.')
        self.__nome = nome

    @property
    def catalogo(self):
        """Retorna o catálogo principal de jogos."""
        return self.__catalogo

    @property
    def colecoes(self):
        """Retorna a lista de coleções do usuário."""
        return self.__colecoes.copy()

    # Operações

    def adicionar_jogo(self, jogo: Jogo):
        """Adiciona um jogo ao catálogo principal."""
        self.__catalogo.adicionar_jogo(jogo)

    def remover_jogo(self, jogo: Jogo):
        """Remove um jogo do catálogo principal."""
        self.__catalogo.remover_jogo(jogo)


    def tempo_total_jogado(self):
        """Calcula o tempo total jogado."""
        return self.__catalogo.total_horas()


    def __str__(self):
        """Retorna a representação textual do usuário."""
        return(f'Usuário {self.nome} | Qnt de jogos: {len(self.catalogo.jogos)}')
