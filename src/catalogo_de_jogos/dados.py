import json
from datetime import date
from catalogo_de_jogos.jogo import JogoPc, JogoConsole, JogoMobile
from catalogo_de_jogos.statusjogo import StatusJogo
from catalogo_de_jogos.usuario import Usuario


def jogo_dict(jogo):
    return {
        'tipo': jogo.plataforma,
        'titulo': jogo.titulo,
        'genero': jogo.genero,
        'plataforma': jogo.plataforma,
        'horas_jogadas': jogo.horas_jogadas,
        'status': jogo.status.name,
        'nota': jogo.nota,
        'data_inicio': jogo.data_inicio.isoformat() if jogo.data_inicio else None,
        'data_fim': jogo.data_fim.isoformat() if jogo.data_fim else None
    }

def dict_jogo(dados):
    tipo = dados ['tipo']

    if tipo == 'PC':
        jogo = JogoPc(dados['titulo'], dados['genero'])
    elif tipo == 'Console':
        jogo = JogoConsole(dados['titulo'], dados['genero'], 'Console')
    else:
        jogo = JogoMobile(dados['titulo'], dados['genero'])

    jogo.adicionar_horas(dados['horas_jogadas'])
    jogo.status = StatusJogo[dados['status']]

    if dados['status'] == 'FINALIZADO' and dados['nota'] is not None:
        jogo.avaliar(dados['nota'])


    jogo._Jogo__data_inicio = (
        date.fromisoformat(dados["data_inicio"])
        if dados["data_inicio"] else None
    )
    jogo._Jogo__data_fim = (
        date.fromisoformat(dados["data_fim"])
        if dados["data_fim"] else None
    )

    return jogo


# Salva o catalogo do JSON
def salvar_usuarios(usuarios, caminho="dados.json"):
    dados = {
        "usuarios": [
            {
                "nome": u.nome,
                "jogos": [jogo_dict(j) for j in u.catalogo.jogos]
            }
            for u in usuarios
        ]
    }

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)



# Carregar o catálogo do JSON

def carregar_usuarios(caminho="dados.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    usuarios = []

    for u in dados["usuarios"]:
        usuario = Usuario(u["nome"])
        for jogo_dict in u["jogos"]:
            usuario.adicionar_jogo(dict_jogo(jogo_dict))
        usuarios.append(usuario)

    return usuarios
