class Usuario:
    def __init__(self, nome, tipo_de_jogador):
        self.nome = nome
        self.tipo_de_jogador = tipo_de_jogador
        self.catalogo = CatalogoJogos()
        self.colecoes = []

    def adicionar_jogo(self, jogo):
        self.catalogo.adicionar_jogo(jogo)

    def calcular_tempo_total_jogado(self):
        return self.catalogo.total_horas()

    def gerar_relatorio_pessoal(self):
        return {
            "usuario": self.nome,
            "tempo_total": self.calcular_tempo_total_jogado(),
            "total_jogos": len(self.catalogo.listar_jogos())
        }
