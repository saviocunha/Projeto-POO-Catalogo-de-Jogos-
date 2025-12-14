# 📊 Catálogo de Jogos
------------------------------------------------------------------------
## 🧩 Visão Geral
O projeto consiste no desenvolvimento, em Python, de um sistema para gerenciamento de um catálogo pessoal de jogos digitais, permitindo o cadastro, acompanhamento de progresso, organização por categorias e geração de relatórios estatísticos

------------------------------------------------------------------------

## 📝 Principais Classes do Sistema
1. Jogo 
    Classe base responsável por representar um jogo genérico no catálogo. Contém os atributos e métodos comuns a todos os tipos de jogos, garantindo o encapsulamento e as validações básicas.
   Classe Jogo (Classe Base)

    Classe genérica que representa um jogo digital.

-   Atributos: título; gênero; plataforma status (não iniciado, jogando, finalizado); tempo_jogado; data_inicio; data_fim.
-   Métodos: iniciar_jogo(); atualizar_tempo(); finalizar_jogo(); reiniciar_jogo(); exibir_detalhes().
  
2. Classes JogoPC, JogoConsole e JogoMobile
    Herdam da classe Jogo definindo a plataforma específica e podendo incluir atributos ou métodos próprios de cada plataforma.
   
3. Catálogo de Jogos
   Gerencia a coleção principal de jogos. Centralizará as operações de CRUD, filtros (por gênero, plataforma, status), buscas, ordenação e a geração dos relatórios exigidos (total de horas, média de notas, percentuais, top 5, etc). Essa classe também aplica regras importantes, como impedir jogos duplicados (mesmo título e plataforma) e limitar a quantidade de jogos com status “JOGANDO”.
   
4.  Coleção
    A classe Colecao é responsável por agrupar listas personalizadas de jogos.

5. Usuário
    Representa o usuário do sistema. Um usuário pode possuir um catálogo de jogos e diversas coleções personalizadas.

    O sistema Catálogo de Jogos Digitais tem como objetivo permitir que usuários registrem, acompanhem e analisem seu progresso em jogos digitais, aplicando conceitos de Programação Orientada a Objetos, como encapsulamento, herança simples e múltipla, métodos especiais e regras de negócio configuráveis.
   
    5.1 Classe Usuário
   
    Representa a pessoa que utiliza o sistema e gerencia seu catálogo de jogos.
-   Atributos:nome;  tipo_de_jogador (casual, competitivo, hardcore, etc); tempo_total_jogado; lista_de_jogos
-   Métodos: adicionar_jogo(); remover_jogo(); listar_jogos(); calcular_tempo_total_jogado(); gerar_relatorio_pessoal()

7. Classes do Sistema

8. Classe Relatorio
    Responsável por gerar estatísticas e informações consolidadas do catálogo, como total de horas jogadas, percentual de jogos por status e lista dos jogos mais jogados.

9. Configuracoes
   Gerenciar as configurações do usuário (meta anual, gêneros favoritos, limite de jogos simultâneos) lidas e salvas no settings.json.
   
------------------------------------------------------------------------

## 👨‍💻 Desenvolvedores


#### 👤 José Eudásio de Monte Viana  | 📧 **Email:** jeviana2020@gmail.com  


#### 👤 Francisco Diogo de Sousa Silva  | 📧 **Email:** sousa.diogo@aluno.ufca.edu.br  


#### 👤 Francisco Sávio Sousa da Cunha  | 📧 **Email:** savio.cunha@aluno.ufca.edu.br  


------------------------------------------------------------------------
## ✒️ Atribuições de cada desenvolvedor

As responsabilidades de cada desenvolvedor está detalhada a seguir:

- *Sávio:* responsável pela modelagem das classes Jogo e suas especializações, implementação da herança, encapsulamento com @property e métodos especiais exigidos pelo projeto.

- *Diogo:* responsável pelo gerenciamento do catálogo e das coleções, implementação de filtros, ordenações e aplicação das principais regras de negócio do sistema.

- *Eudásio:* responsável pela persistência dos dados, leitura das configurações do sistema, geração de relatórios estatísticos, implementação dos testes automatizados e apoio na documentação do projeto .

Estratégias para a execução do projeto
 - Utilizaremos Git/GitHub com um repositório único.
 - Realizaremos reuniões de sincronização via Google Meet para alinhamento e integração das partes do código.


------------------------------------------------------------------------

## 📌 Requisitos

-   Python **3.10+**\
-   Nenhuma dependência externa

------------------------------------------------------------------------
