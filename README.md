# 📊 Catálogo de Jogos
------------------------------------------------------------------------
## 🧩 Visão Geral
O projeto consiste no desenvolvimento, em Python, de um sistema para gerenciamento de um catálogo pessoal de jogos digitais, permitindo o cadastro, acompanhamento de progresso, organização por categorias e geração de relatórios estatísticos

------------------------------------------------------------------------

## 📝 Principais Classes do Sistema

1. Jogo 
    Classe base responsável por representar um jogo genérico no catálogo. Contém os atributos e métodos comuns a todos os tipos de jogos, garantindo o encapsulamento e as validações básicas.
   
3. Classes JogoPC, JogoConsole e JogoMobile
    Herdam da classe Jogo definindo a plataforma específica e podendo incluir atributos ou métodos próprios de cada plataforma.
   
4. Catálogo de Jogos
   Gerencia a coleção principal de jogos. Centralizará as operações de CRUD, filtros (por gênero, plataforma, status), buscas, ordenação e a geração dos relatórios exigidos (total de horas, média de notas, percentuais, top 5, etc). Essa classe também aplica regras importantes, como impedir jogos duplicados (mesmo título e plataforma) e limitar a quantidade de jogos com status “JOGANDO”.
   
6.  Coleção
    A classe Colecao é responsável por agrupar listas personalizadas de jogos.

7. Usuário
    Representa o usuário do sistema. Um usuário pode possuir um catálogo de jogos e diversas coleções personalizadas.
   
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
