
import pytest
from catalogo_de_jogos.jogo import JogoPc
from catalogo_de_jogos.usuario import Usuario
from catalogo_de_jogos.colecao import Colecao
from catalogo_de_jogos.statusjogo import StatusJogo
from catalogo_de_jogos.relatorios import (
    total_horas,
    media_avaliacoes,
    top_5_mais_jogados
)
from catalogo_de_jogos.dados import salvar_usuarios, carregar_usuarios


# ---------------- JOGO ----------------

def test_criar_jogo():
    jogo = JogoPc("Hades", "Roguelike")
    assert jogo.horas_jogadas == 0
    assert jogo.status == StatusJogo.NAO_INICIADO


def test_adicionar_horas():
    jogo = JogoPc("Hades", "Roguelike")
    jogo.adicionar_horas(3)
    assert jogo.horas_jogadas == 3
    assert jogo.status == StatusJogo.JOGANDO


def test_finalizar_sem_horas():
    jogo = JogoPc("Hades", "Roguelike")
    with pytest.raises(ValueError):
        jogo.finalizar()


# ---------------- USUÁRIO ----------------

def test_usuario_adiciona_jogo():
    usuario = Usuario("Sávio")
    jogo = JogoPc("Hades", "Roguelike")
    usuario.adicionar_jogo(jogo)
    assert jogo in usuario.catalogo.jogos


# ---------------- COLEÇÃO ----------------

def test_colecao_nao_aceita_duplicado():
    colecao = Colecao("Favoritos")
    jogo = JogoPc("Hades", "Roguelike")
    colecao.adicionar_jogo(jogo)

    with pytest.raises(ValueError):
        colecao.adicionar_jogo(jogo)


# ---------------- RELATÓRIOS ----------------

def test_total_horas():
    usuario = Usuario("Sávio")
    jogo = JogoPc("Hades", "Roguelike")
    jogo.adicionar_horas(5)
    usuario.adicionar_jogo(jogo)

    assert total_horas(usuario) == 5


def test_media_avaliacoes():
    usuario = Usuario("Sávio")
    jogo = JogoPc("Hades", "Roguelike")
    jogo.adicionar_horas(2)
    jogo.finalizar()
    jogo.avaliar(8)

    usuario.adicionar_jogo(jogo)
    assert media_avaliacoes(usuario) == 8


