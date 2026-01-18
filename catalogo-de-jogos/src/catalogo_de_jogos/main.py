
from .dados import carregar_usuarios, salvar_usuarios
from .cli import executar_sistema


def main():
    """Função principal que gerencia o fluxo da aplicação."""
    # 1️⃣ Carregar dados persistidos
    try:
        usuarios = carregar_usuarios()
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        usuarios = []
        print("Nenhum dado encontrado. Iniciando sistema vazio.")

    # 2️⃣ Executar interface em linha de comando
    executar_sistema(usuarios)

    # 3️⃣ Salvar dados antes de encerrar
    salvar_usuarios(usuarios)
    print("Dados salvos com sucesso.")


if __name__ == "__main__":
    main()

