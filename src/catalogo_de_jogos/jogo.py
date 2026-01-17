from datetime import date

from catalogo_de_jogos.statusjogo import StatusJogo


# --------------- Classe Base --------------- 

class Jogo:
    def __init__(self, titulo: str, genero:str, plataforma: str):
        # Atributos que são validados via setter 
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        # Atributos de Estado Interno --> Não foram criados setters
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
    def titulo(self,value):
        if value == None or value.strip() == '':
            raise ValueError('O título não pode ser vazio!')
        self.__titulo = value.strip()
        

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        if value == None or value.strip() == '':
            raise ValueError('O gênero do jogo não pode ser vazio.')
        self.__genero = value.strip()
    
    @property
    def plataforma(self):
        return self.__plataforma
    
    @plataforma.setter
    def plataforma(self, value):
        if value == None or value.strip() == '':
            raise ValueError('Plataforma não pode ser vazia.')
        self.__plataforma = value.strip()
    

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
    
    
    @property
    def data_fim(self):
        return self.__data_fim
    
   
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, value):
        if self.__status != StatusJogo.FINALIZADO:
            raise ValueError('Só é possivel avaliar jogos finalizados! ')
        if not (0 <= value <= 10):
            raise ValueError('Nota deve ser de 0 a 10.')
        self.__nota = value


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
            raise ValueError('Não é possivel finalizar o jogo sem horas jogadas. ')
        
        self.__status = StatusJogo.FINALIZADO
        self.__data_fim = date.today()
    
    def reiniciar(self):
        self.__status = StatusJogo.NAO_INICIADO
        self.__horas_jogadas = 0.0
        self.__nota = None
        self.__data_inicio = None
        self.__data_fim = None
    
    def avaliar(self, value: float): # Utiliza o setter para validar a nota
        self.nota = value


#  --------------- Métodos Especiais  ---------------        

    def __str__(self):
        return (f'{self.titulo} - {self.plataforma}')
    
    def __repr__(self):
        return (f' Jogo (Título = {self.titulo}, Plataforma = {self.plataforma}, Horas = {self.horas_jogadas}, Status = {self.status.name}, Nota = {self.nota})')


    def __eq__(self, value):
        return isinstance(value, Jogo) and \
                self.titulo.lower() == value.titulo.lower() and \
                self.plataforma == value.plataforma


    def __lt__(self, value):
        return self.horas_jogadas < value.horas_jogadas

   

# --------------- Classes Filhas --------------- 
class JogoPc(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, plataforma = 'PC')   

class JogoConsole(Jogo):
    def __init__(self, titulo, genero, nome_console):
        super().__init__(titulo, genero, plataforma = 'Console')
        self.nome_console = nome_console
    

    @property
    def nome_console(self):
        return self.__nome_console
    
    @nome_console.setter
    def nome_console(self, nome):
        if nome == None or nome.strip() == '':
            raise ValueError('Deve ser informado o nome do console.')
        self.__nome_console = nome
   

class JogoMobile(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, plataforma = 'Mobile')



