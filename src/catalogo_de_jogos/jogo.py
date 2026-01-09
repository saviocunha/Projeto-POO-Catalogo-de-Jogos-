from datetime import date

from statusjogo import StatusJogo


# --------------- Classe Base --------------- 

class Jogo:
    def __init__(self, titulo: str, genero:str, plataforma: str):
        self.__titulo = titulo
        self.__genero = genero
        self.__plataforma = plataforma

        self.__horas_jogadas = 0.0
        self.__status = StatusJogo.NAO_INICIADO
        self.__data_inicio = None
        self.__data_fim = None
        self.__nota = None
        


# --------------- Properties - Getters /Setters --------------- 


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
    
    # OBS.: Não foi definido setter para o atributo __horas_jogadas.
    # Consultar a função adicionar_horas na seção "Regras de Negócio"
      
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if isinstance(novo_status, StatusJogo):
            self.__status = novo_status
        else:
            raise ValueError(f"O status deve ser um valor do tipo StatusJogo. Recebido: {type(novo_status)}")
    
    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self, data):
        self.__data_inicio = data
    
    @property
    def data_fim(self):
        return self.__data_fim
    
    @data_fim.setter
    def data_fim(self, data):
        self.__data_fim = data

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, valor):
        if self.status != StatusJogo.FINALIZADO:
            raise ValueError('Só é possivel avaliar jogos finalizados! ')
        if not (0 <= valor <= 10):
            raise ValueError('Nota deve ser de 0 a 10.')
        self.__nota = valor


#  --------------- Regras de Negócio  --------------- 
    
    def adicionar_horas(self, horas: float):
        if horas < 0:
            raise ValueError('Horas não podem ser negativas.')
        
        self.__horas_jogadas += horas

        if self.__status == StatusJogo.NAO_INICIADO:
            self.__status = StatusJogo.JOGANDO
            self.__data_inicio = date.today()
    

    def finalizar(self):
        if self.__horas_jogadas < 1:
            raise ValueError('Não é possivel finalizar com menos de 1 h de jogada. ')
        
        self.__status = StatusJogo.FINALIZADO
        self.__data_fim = date.today()
    
    def reiniciar(self):
        self.__horas_jogadas = 0
        self.__nota = None
        self.__status = StatusJogo.JOGANDO
        self.__data_inicio = date.today()
        self.__data_fim = None
    
    def avaliar(self, valor = float):
        if self.__status != StatusJogo.FINALIZADO:
            raise ValueError('Só é possivel avalizar jogos finalizados.')
        
        if not(0 <= valor <= 10):
            raise ValueError('Nota deve estar entre 0 e 10')
        self.__nota = valor


#  --------------- Métodos Especiais  ---------------        

    def __str__(self):
        return (f'{self.titulo} - {self.plataforma}')
    
    def __repr__(self):
        return (f' Jogo (Título = {self.titulo}, Plataforma = {self.plataforma}, Horas = {self.horas_jogadas}, Status = {self.status.name}, Nota = {self.nota})')


    def __eq__(self, valor):
        return isinstance(valor, Jogo) and \
                self.titulo.lower() == valor.titulo.lower() and \
                self.plataforma == valor.plataforma


    def __lt__(self, valor):
        return self.horas_jogadas < valor.horas_jogadas

   

# --------------- Classes Filhas --------------- 
class JogoPc(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, plataforma = 'PC')   

class JogoConsole(Jogo):
    def __init__(self, titulo, genero, nome_console):
        super().__init__(titulo, genero, plataforma = 'Console')
        self.__nome_console = nome_console
    

    @property
    def nome_console(self):
        return self.__nome_console
    
    @nome_console.setter
    def nome_console(self, nome):
        if nome == '':
            raise ValueError('Deve ser informado o nome do console.')
        self.__nome_console = nome
   

class JogoMobile(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, plataforma = 'Mobile')



