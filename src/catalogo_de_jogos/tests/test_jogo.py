import pytest
from jogo import Jogo, JogoPc, JogoConsole, JogoMobile, StatusJogo


# =========================
# Testes da classe Jogo
# =========================

def test_criacao_jogo_valido():
    jogo = Jogo("The Witcher 3", "RPG", "PC")

    assert jogo.titulo == "The Witcher 3"
    assert jogo.genero == "RPG"
    assert jogo.plataforma == "PC"
    assert jogo.horas_jogadas == 0.0
    assert jogo.status == StatusJogo.NAO_INICIADO
    assert jogo.data_inicio is None
    assert jogo.data_fim is None
    assert jogo.nota is None


def test_adicionar_horas_valor_positivo():
    jogo = Jogo("Teste", "Ação", "PC")

    jogo.adicionar_horas(3)

    assert jogo.horas_jogadas == 3
    assert jogo.status == StatusJogo.JOGANDO
    assert jogo.data_inicio is not None


def test_adicionar_horas_negativas_levanta_excecao():
    jogo = Jogo("Teste", "Ação", "PC")

    with pytest.raises(ValueError, match="Horas não podem ser negativas"):
        jogo.adicionar_horas(-1)


def test_finalizar_jogo_sem_horas_levanta_excecao():
    jogo = Jogo("Teste", "Ação", "PC")

    with pytest.raises(ValueError):
        jogo.finalizar()


def test_finalizar_jogo_valido():
    jogo = Jogo("Teste", "Ação", "PC")
    jogo.adicionar_horas(2)

    jogo.finalizar()

    assert jogo.status == StatusJogo.FINALIZADO
    assert jogo.data_fim is not None


def test_avaliar_jogo_nao_finalizado_levanta_excecao():
    jogo = Jogo("Teste", "Ação", "PC")

    with pytest.raises(ValueError):
        jogo.avaliar(8)


def test_avaliar_jogo_com_nota_invalida():
    jogo = Jogo("Teste", "Ação", "PC")
    jogo.adicionar_horas(2)
    jogo.finalizar()

    with pytest.raises(ValueError):
        jogo.avaliar(11)


def test_avaliar_jogo_valido():
    jogo = Jogo("Teste", "Ação", "PC")
    jogo.adicionar_horas(2)
    jogo.finalizar()

    jogo.avaliar(9)

    assert jogo.nota == 9


def test_reiniciar_jogo():
    jogo = Jogo("Teste", "Ação", "PC")
    jogo.adicionar_horas(3)
    jogo.finalizar()
    jogo.avaliar(8)

    jogo.reiniciar()

    assert jogo.horas_jogadas == 0
    assert jogo.status == StatusJogo.NAO_INICIADO
    assert jogo.data_inicio is None
    assert jogo.data_fim is None
    assert jogo.nota is None


def test_igualdade_jogos():
    jogo1 = Jogo("The Witcher 3", "RPG", "PC")
    jogo2 = Jogo("the witcher 3", "RPG", "PC")
    jogo3 = Jogo("The Witcher 3", "RPG", "Console")

    assert jogo1 == jogo2
    assert jogo1 != jogo3


def test_comparacao_menor_que():
    jogo1 = Jogo("Jogo 1", "Ação", "PC")
    jogo2 = Jogo("Jogo 2", "Ação", "PC")

    jogo1.adicionar_horas(2)
    jogo2.adicionar_horas(5)

    assert jogo1 < jogo2


# =========================
# Testes das subclasses
# =========================

def test_jogo_pc():
    jogo = JogoPc("Hades", "Roguelike")

    assert jogo.plataforma == "PC"


def test_jogo_console():
    jogo = JogoConsole("Zelda", "Aventura", "Nintendo Switch")

    assert jogo.plataforma == "Console"
    assert jogo.nome_console == "Nintendo Switch"


def test_jogo_console_nome_vazio_levanta_excecao():
    with pytest.raises(ValueError, match="Deve ser informado o nome do console"):
        JogoConsole("Zelda", "Aventura", "")


def test_jogo_mobile():
    jogo = JogoMobile("Candy Crush", "Puzzle")

    assert jogo.plataforma == "Mobile"
