from datetime import date

from catalogo_de_jogos.statusjogo import StatusJogo


# --------------- Classe Base --------------- 

class Jogo:
    def __init__(self, titulo: str, genero:str, plataforma: str):
        """Inicializa um novo jogo."""
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
        """Retorna o título do jogo."""
        return self.__titulo

    @titulo.setter
    def titulo(self,value):
        """Define o título do jogo com validação."""
        if value == None or value.strip() == '':
            raise ValueError('O título não pode ser vazio!')
        self.__titulo = value.strip()
        

    @property
    def genero(self):
        """Retorna o gênero do jogo."""
        return self.__genero

    @genero.setter
    def genero(self, value):
        """Define o gênero do jogo com validação."""
        if value == None or value.strip() == '':
            raise ValueError('O gênero do jogo não pode ser vazio.')
        self.__genero = value.strip()
    
    @property
    def plataforma(self):
        """Retorna a plataforma do jogo."""
        return self.__plataforma
    
    @plataforma.setter
    def plataforma(self, value):
        """Define a plataforma do jogo com validação."""
        if value == None or value.strip() == '':
            raise ValueError('Plataforma não pode ser vazia.')
        self.__plataforma = value.strip()
    

    @property
    def horas_jogadas(self):
        """Retorna o total de horas jogadas."""
        return self.__horas_jogadas
    
    # OBS.: Não foi definido setter para o atributo __horas_jogadas.
    # Consultar a função adicionar_horas na seção "Regras de Negócio"
      
    @property
    def status(self):
        """Retorna o status atual do jogo."""
        return self.__status

    @status.setter
    def status(self, novo_status):
        """Define o status do jogo."""
        if isinstance(novo_status, StatusJogo):
            self.__status = novo_status
        else:
            raise ValueError(f"O status deve ser um valor do tipo StatusJogo. Recebido: {type(novo_status)}")
    
    @property
    def data_inicio(self):
        """Retorna a data de início do jogo."""
        return self.__data_inicio
    
    
    @property
    def data_fim(self):
        """Retorna a data de fim do jogo."""
        return self.__data_fim
    
   
    @property
    def nota(self):
        """Retorna a nota atribuída ao jogo."""
        return self.__nota
    
    @nota.setter
    def nota(self, value):
        """Define a nota do jogo com validação."""
        if self.__status != StatusJogo.FINALIZADO:
            raise ValueError('Só é possivel avaliar jogos finalizados! ')
        if not (0 <= value <= 10):
            raise ValueError('Nota deve ser de 0 a 10.')
        self.__nota = value


#  --------------- Regras de Negócio  --------------- 
    
    def adicionar_horas(self, horas: float):
        """Adiciona horas de jogo e atualiza o status."""
        if horas < 0:
            raise ValueError('Horas não podem ser negativas.')
        
        self.__horas_jogadas += horas

        if self.__status == StatusJogo.NAO_INICIADO:
            self.__status = StatusJogo.JOGANDO
            self.__data_inicio = date.today()
    

    def finalizar(self):
        """Marca o jogo como finalizado."""
        if self.__horas_jogadas < 1:
            raise ValueError('Não é possivel finalizar o jogo sem horas jogadas. ')
        
        self.__status = StatusJogo.FINALIZADO
        self.__data_fim = date.today()
    
    def reiniciar(self):
        """Reinicia o progresso do jogo."""
        self.__status = StatusJogo.NAO_INICIADO
        self.__horas_jogadas = 0.0
        self.__nota = None
        self.__data_inicio = None
        self.__data_fim = None
    
    def avaliar(self, value: float): # Utiliza o setter para validar a nota
        """Atribui uma nota ao jogo."""
        self.nota = value


#  --------------- Métodos Especiais  ---------------        

    def __str__(self):
        """Retorna uma representação simples em string."""
        return (f'{self.titulo} - {self.plataforma}')
    
    def __repr__(self):
        """Retorna uma representação detalhada em string."""
        return (f' Jogo (Título = {self.titulo}, Plataforma = {self.plataforma}, Horas = {self.horas_jogadas}, Status = {self.status.name}, Nota = {self.nota})')


    def __eq__(self, value):
        """Verifica igualdade entre dois jogos."""
        return isinstance(value, Jogo) and \
                self.titulo.lower() == value.titulo.lower() and \
                self.plataforma == value.plataforma


    def __lt__(self, value):
        """Compara jogos por horas jogadas."""
        return self.horas_jogadas < value.horas_jogadas

   

# --------------- Classes Filhas --------------- 
class JogoPc(Jogo):
    def __init__(self, titulo, genero):
        """Inicializa um jogo de PC."""
        super().__init__(titulo, genero, plataforma = 'PC')   

class JogoConsole(Jogo):
    def __init__(self, titulo, genero, nome_console):
        """Inicializa um jogo de Console."""
        super().__init__(titulo, genero, plataforma = 'Console')
        self.nome_console = nome_console
    

    @property
    def nome_console(self):
        """Retorna o nome do console."""
        return self.__nome_console
    
    @nome_console.setter
    def nome_console(self, nome):
        """Define o nome do console com validação."""
        if nome == None or nome.strip() == '':
            raise ValueError('Deve ser informado o nome do console.')
        self.__nome_console = nome
   

class JogoMobile(Jogo):
    def __init__(self, titulo, genero):
        """Inicializa um jogo Mobile."""
        super().__init__(titulo, genero, plataforma = 'Mobile')



