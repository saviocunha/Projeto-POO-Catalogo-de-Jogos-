from datetime import date

from jogo import JogoPc, JogoConsole, JogoMobile
from statusjogo import StatusJogo
from colecao import Colecao
from usuario import Usuario



def main():
    # Criar usuário
    usuario = Usuario("Sávio")
    print(usuario)

    # Criar jogo
    jogo = JogoPc("Hades", "Roguelike")
    print(jogo)

    # Adicionar jogo ao catálogo
    usuario.adicionar_jogo(jogo)
    print(f"Jogos no catálogo: {len(usuario.catalogo.jogos)}")

    # Adicionar horas
    jogo.adicionar_horas(5)
    print(f"Horas jogadas: {jogo.horas_jogadas}")
    print(f"Status: {jogo.status.name}")

    # Finalizar e avaliar
    jogo.finalizar()
    jogo.avaliar(9)
    print(f"Nota: {jogo.nota}")


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()

