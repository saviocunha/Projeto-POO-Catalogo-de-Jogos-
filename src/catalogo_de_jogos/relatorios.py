
from catalogo_de_jogos.statusjogo import StatusJogo


def total_horas(usuario):
    return usuario.tempo_total_jogado()


def percentual_por_status(usuario):
    jogos = usuario.catalogo.jogos
    total = len(jogos)

    if total == 0:
        return {}

    resultado = {}
    for status in StatusJogo:
        qtd = len([j for j in jogos if j.status == status])
        resultado[status.name] = (qtd / total) * 100

    return resultado


def media_avaliacoes(usuario):
    finalizados = [
        j for j in usuario.catalogo.jogos
        if j.status == StatusJogo.FINALIZADO and j.nota is not None
    ]

    if not finalizados:
        return None

    return sum(j.nota for j in finalizados) / len(finalizados)


def top_5_mais_jogados(usuario):
    jogos = sorted(
        usuario.catalogo.jogos,
        reverse=True
    )
    return jogos[:5]


def jogos_por_plataforma(usuario):
    resultado = {}

    for jogo in usuario.catalogo.jogos:
        plataforma = jogo.plataforma
        resultado[plataforma] = resultado.get(plataforma, 0) + 1

    return resultado


def jogos_por_genero(usuario):
    resultado = {}

    for jogo in usuario.catalogo.jogos:
        genero = jogo.genero
        resultado[genero] = resultado.get(genero, 0) + 1

    return resultado


def exibir_relatorios(usuario):
    print("\n=== RELATÓRIOS DO USUÁRIO ===")

    # Total de horas
    print(f"Total de horas jogadas: {total_horas(usuario):.1f}h")

    # Média de avaliações
    media = media_avaliacoes(usuario)
    if media is not None:
        print(f"Média das avaliações (finalizados): {media:.1f}")
    else:
        print("Nenhum jogo finalizado com avaliação.")

    # Percentual por status
    print("\nPercentual de jogos por status:")
    percentuais = percentual_por_status(usuario)
    for status, valor in percentuais.items():
        print(f"- {status}: {valor:.1f}%")

    # Jogos por plataforma
    print("\nJogos por plataforma:")
    for plataforma, qtd in jogos_por_plataforma(usuario).items():
        print(f"- {plataforma}: {qtd}")

    # Jogos por gênero
    print("\nJogos por gênero:")
    for genero, qtd in jogos_por_genero(usuario).items():
        print(f"- {genero}: {qtd}")

    # Top 5
    print("\nTop 5 jogos mais jogados:")
    top5 = top_5_mais_jogados(usuario)
    if not top5:
        print("Nenhum jogo cadastrado.")
    else:
        for i, jogo in enumerate(top5, start=1):
            print(f"{i}. {jogo} - {jogo.horas_jogadas}h")

