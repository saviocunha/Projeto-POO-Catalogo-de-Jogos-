import pytest
from catalogo_de_jogos.jogo import JogoPc
from catalogo_de_jogos.statusjogo import StatusJogo


def test_criar_jogo_inicia_nao_iniciado():
    jogo = JogoPc("Hades", "Roguelike")
    assert jogo.status == StatusJogo.NAO_INICIADO
    assert jogo.horas_jogadas == 0


def test_adicionar_horas_altera_status():
    jogo = JogoPc("Hades", "Roguelike")
    jogo.adicionar_horas(2)
    assert jogo.horas_jogadas == 2
    assert jogo.status == StatusJogo.JOGANDO


def test_finalizar_sem_horas_dispara_erro():
    jogo = JogoPc("Hades", "Roguelike")
    with pytest.raises(ValueError):
        jogo.finalizar()


def test_avaliar_apenas_finalizado():
    jogo = JogoPc("Hades", "Roguelike")
    jogo.adicionar_horas(2)
    jogo.finalizar()
    jogo.avaliar(9)
    assert jogo.nota == 9
