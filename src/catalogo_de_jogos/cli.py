
from .jogo import JogoPc, JogoConsole, JogoMobile
from .statusjogo import StatusJogo
from .usuario import Usuario
from .relatorios import exibir_relatorios



# =======================
# MENU DE USUÁRIOS
# =======================

def menu_usuarios():
    print("\n=== USUÁRIOS ===")
    print("1 - Escolher usuário")
    print("2 - Cadastrar novo usuário")
    print("0 - Sair")
    return input("Opção: ")


def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario.nome}")


def escolher_usuario(usuarios):
    listar_usuarios(usuarios)

    try:
        opcao = int(input("Escolha o número do usuário: "))
        return usuarios[opcao - 1]
    except (ValueError, IndexError):
        print("Usuário inválido.")
        return None


def cadastrar_usuario(usuarios):
    nome = input("Nome do novo usuário: ").strip()

    if not nome:
        print("Nome inválido.")
        return None

    if any(u.nome.lower() == nome.lower() for u in usuarios):
        print("Usuário já existe.")
        return None

    usuario = Usuario(nome)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario


# =======================
# MENU DE JOGOS
# =======================

def menu_jogos(usuario):
    print(f"\n=== CATÁLOGO DE JOGOS ({usuario.nome}) ===")
    print("1 - Cadastrar jogo")
    print("2 - Listar jogos")
    print("3 - Atualizar progresso")
    print("4 - Finalizar jogo")
    print("5 - Relatórios")
    print("0 - Voltar")
    return input("Opção: ")


def cadastrar_jogo(usuario):
    print("\nCadastro de Jogo")

    titulo = input("Título: ")
    genero = input("Gênero: ")
    plataforma = input("Plataforma (PC / Console / Mobile): ").upper()

    if plataforma == "PC":
        jogo = JogoPc(titulo, genero)
    elif plataforma == "CONSOLE":
        console = input("Nome do console: ")
        jogo = JogoConsole(titulo, genero, console)
    elif plataforma == "MOBILE":
        jogo = JogoMobile(titulo, genero)
    else:
        print("Plataforma inválida.")
        return

    try:
        usuario.adicionar_jogo(jogo)
        print("Jogo cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")


def listar_jogos(usuario):
    if not usuario.catalogo.jogos:
        print("Nenhum jogo cadastrado.")
        return

    for i, jogo in enumerate(usuario.catalogo.jogos, start=1):
        print(
            f"{i}. {jogo} | "
            f"Status: {jogo.status.name} | "
            f"Horas: {jogo.horas_jogadas}"
        )


def atualizar_progresso(usuario):
    listar_jogos(usuario)

    try:
        indice = int(input("Escolha o número do jogo: ")) - 1
        jogo = usuario.catalogo.jogos[indice]

        horas = float(input("Horas a adicionar: "))
        jogo.adicionar_horas(horas)

        print("Progresso atualizado.")
    except (ValueError, IndexError) as e:
        print("Entrada inválida.")


def finalizar_jogo(usuario):
    listar_jogos(usuario)

    try:
        indice = int(input("Escolha o número do jogo: ")) - 1
        jogo = usuario.catalogo.jogos[indice]

        jogo.finalizar()
        nota = float(input("Nota (0 a 10): "))
        jogo.avaliar(nota)

        print("Jogo finalizado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")
    except IndexError:
        print("Jogo inválido.")



# =======================
# EXECUÇÃO DO SISTEMA
# =======================

def executar_cli(usuario):
    while True:
        opcao = menu_jogos(usuario)

        if opcao == "1":
            cadastrar_jogo(usuario)
        elif opcao == "2":
            listar_jogos(usuario)
        elif opcao == "3":
            atualizar_progresso(usuario)
        elif opcao == "4":
            finalizar_jogo(usuario)
        elif opcao == "5":
            exibir_relatorios(usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def executar_sistema(usuarios):
    while True:
        opcao = menu_usuarios()

        if opcao == "1":
            usuario = escolher_usuario(usuarios)
            if usuario:
                executar_cli(usuario)

        elif opcao == "2":
            usuario = cadastrar_usuario(usuarios)
            if usuario:
                executar_cli(usuario)

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")

