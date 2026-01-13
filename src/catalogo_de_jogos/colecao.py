from jogo import Jogo

class Colecao:
    def __init__(self, nome: str):
        self.nome = nome
        self.__jogos = []
   
    @property
    def nome(self):
        self.__nome = nome

    @nome.setter
    def nome(self, value)   :
        if value == None or value.strip()=='':
            raise ValueError('O nome não pode ser vazio.')
        self.__nome = value

    
    @property
    def jogos(self):
        return self.__jogos.copy()




    def adicionar_jogo(self, jogo: Jogo):
        if jogo in self.__jogos:
            raise ValueError('Jogo já cadastrado!')
        self.__jogos.append(jogo)

    def remover_jogo(self, jogo: Jogo):
        self.__jogos.remove(jogo)

    def total_horas(self):
        return sum(jogo.horas_jogadas for jogo in self.__jogos)
