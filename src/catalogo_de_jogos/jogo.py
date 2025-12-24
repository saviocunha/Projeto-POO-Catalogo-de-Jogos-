
class jogo:
    def __init__(self, titulo: str, genero:str):
        self.__titulo = titulo
        self.__genero = genero
        


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




class jogo_pc(jogo):
    pass

class jogo_console(jogo):
    pass

class jogo_mobile(jogo):
    pass