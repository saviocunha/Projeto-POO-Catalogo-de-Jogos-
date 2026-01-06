
from enum import Enum
from datetime import date

class jogo:
    def __init__(self, titulo: str, genero:str, plataforma: str):
        self.__titulo = titulo
        self.__genero = genero
        self.__plataforma = plataforma

        self.__horas_jogadas = 0
        self.__status = StatusJogo.NAO_INICIADO
        self.__data_inicio = None
        self.__data_fim = None
        self.__nota = None
        


# Properties - Getters /Setters


    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        if titulo == '':
            raise ValueError('O título não pode ser vazio!')
        self.__titulo = titulo
        

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    
    @property
    def plataforma(self):
        return self.__plataforma
    
    @plataforma.setter
    def plataforma(self, plataforma):
        self.__plataforma = plataforma
    

    @property
    def horas_jogadas(self):
        return self.__horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, horas_jogadas):
        self.__horas_jogadas = horas_jogadas
    

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if isinstance(novo_status, StatusJogo):
            self.__status = novo_status
        else:
            raise ValueError(f"O status deve ser um valor do tipo StatusJogo. Recebido: {type(novo_status)}")


class jogo_pc(jogo):
    pass

class jogo_console(jogo):
    pass

class jogo_mobile(jogo):
    pass

class StatusJogo(Enum):
    NAO_INICIADO = "NÃO INICIADO"
    JOGANDO = "JOGANDO"
    FINALIZADO = "FINALIZADO"