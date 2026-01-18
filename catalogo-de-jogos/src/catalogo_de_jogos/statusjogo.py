from enum import Enum

# Define os status possiveis dos jogos

class StatusJogo(Enum):
    """Enumeração dos status possíveis de um jogo."""
    NAO_INICIADO = "NÃO INICIADO"
    JOGANDO = "JOGANDO"
    FINALIZADO = "FINALIZADO"
