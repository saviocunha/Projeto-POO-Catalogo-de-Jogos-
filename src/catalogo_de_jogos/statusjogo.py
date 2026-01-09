from enum import Enum

# Define os status possiveis dos jogos

class StatusJogo(Enum):
    NAO_INICIADO = "NÃO INICIADO"
    JOGANDO = "JOGANDO"
    FINALIZADO = "FINALIZADO"
