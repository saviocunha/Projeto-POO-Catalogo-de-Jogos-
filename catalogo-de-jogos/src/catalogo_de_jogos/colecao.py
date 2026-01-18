from .jogo import Jogo

class Colecao:
    def __init__(self, nome: str):
        """Inicializa uma coleção vazia."""
        self.nome = nome
        self.__jogos = []
   
    @property
    def nome(self):
        """Retorna o nome da coleção."""
        self.__nome = nome

    @nome.setter
    def nome(self, value)   :
        """Define o nome da coleção com validação."""
        if value == None or value.strip()=='':
            raise ValueError('O nome não pode ser vazio.')
        self.__nome = value

    
    @property
    def jogos(self):
        """Retorna uma cópia da lista de jogos da coleção."""
        return self.__jogos.copy()




    def adicionar_jogo(self, jogo: Jogo):
        """Adiciona um jogo à coleção."""
        if jogo in self.__jogos:
            raise ValueError('Jogo já cadastrado!')
        self.__jogos.append(jogo)

    def remover_jogo(self, jogo: Jogo):
        """Remove um jogo da coleção."""
        self.__jogos.remove(jogo)

    def total_horas(self):
        """Calcula o total de horas jogadas na coleção."""
        return sum(jogo.horas_jogadas for jogo in self.__jogos)
