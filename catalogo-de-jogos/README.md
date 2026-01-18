# 📊 Catálogo de Jogos
------------------------------------------------------------------------
## 🧩 Visão Geral
O projeto consiste no desenvolvimento, em Python, de um sistema para o gerenciamento de um catálogo pessoal de jogos digitais, permitindo o cadastro, acompanhamento de progresso, organização por categorias e geração de relatórios estatísticos.

O sistema Catálogo de Jogos Digitais tem como objetivo permitir que usuários registrem, acompanhem e analisem seu progresso em jogos digitais, aplicando conceitos de Programação Orientada a Objetos, como encapsulamento, herança simples e múltipla, métodos especiais e regras de negócio configuráveis.

## Objetivos
-   Aplicar conceitos fundamentais de POO na prática.
-   Modelar um sistema utilizando classes, atributos e métodos.
-   Utilizar herança simples e múltipla de forma adequada.
-   Implementar regras de negócio que garantam a consistência dos dados.
-   Organizar o projeto para entrega via repositório GitHub.

------------------------------------------------------------------------
## 🧩 Conceitos de POO Aplicados
-   Encapsulamento: atributos sensíveis são acessados apenas por métodos controlados.

-   Herança Simples: especialização da classe Jogo em diferentes plataformas.

-   Polimorfismo: comportamentos específicos de acordo com o tipo de jogo.

-   Métodos Especiais: utilizados para exibição, comparação e organização dos objetos

## 📝 Principais Classes do Sistema
1. Classe Jogo:
   Classe base responsável por representar um jogo genérico no catálogo. Contém os atributos e métodos comuns a todos os tipos de jogos, garantindo o encapsulamento e as validações básicas.
   
   Classe Jogo (Classe Base), Classe genérica que representa um jogo digital.

-   Atributos: título; gênero; plataforma status (não iniciado, jogando, finalizado); tempo_jogado; data_inicio; data_fim.
-   Métodos: iniciar_jogo(); atualizar_tempo(); finalizar_jogo(); reiniciar_jogo(); exibir_detalhes().
  
2. Classes JogoPC, JogoConsole e JogoMobile: 
     São Classes que herdam da classe Jogo definindo a plataforma específica e podendo incluir atributos ou métodos próprios de cada plataforma.
   
3. Catálogo de Jogos: 
   É a Gerencia a coleção principal de jogos. Centralizará as operações de CRUD, filtros (por gênero, plataforma, status), buscas, ordenação e a geração dos relatórios exigidos (total de horas, média de notas, percentuais, top 5, etc). Essa classe também aplica regras importantes, como impedir jogos duplicados (mesmo título e plataforma) e limitar a quantidade de jogos com status “JOGANDO”.
   
4.  Classe Colecao: 
    A classe Colecao é responsável por agrupar listas personalizadas de jogos.

5. Classe Usuario: 
Representa o usuário do sistema. Pode possuir um catálogo de jogos e diversas coleções personalizadas.
- **Atributos**: nome, tipo_de_jogador, tempo_total_jogado, lista_de_jogos.
- **Métodos**: `adicionar_jogo()`, `remover_jogo()`, `listar_jogos()`, `calcular_tempo_total_jogado()`, `gerar_relatorio_pessoal()`.

6. Classe Relatorio: 
    Responsável por gerar estatísticas e informações consolidadas do catálogo.

   
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

- Python **3.10+**
- Gerenciador de dependências **Poetry**

## 🚀 Instalação e Execução

Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciamento de dependências.

### 1. Instalar Dependências
Na raiz do projeto, execute:

```bash
poetry install
```

### 2. Executar a Aplicação
Para iniciar a interface de linha de comando (CLI):

```bash
poetry run python -m catalogo_de_jogos.main
```

### 3. Executar Testes
Para rodar a suíte de testes automatizados:

```bash
poetry run pytest
```
