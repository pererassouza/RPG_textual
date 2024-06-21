# RPG Textual

Um simples jogo de RPG textual onde você pode escolher entre diferentes classes de personagens e lutar contra inimigos em um campo de batalha.

### Descrição dos Arquivos

#### Diretório `characters`
- `__init__.py`: Inicializa o módulo de personagens, facilitando a importação de classes.
- `character.py`: Define a classe abstrata `Character` que serve como base para todos os personagens, incluindo métodos abstratos que devem ser implementados pelas subclasses.
- `enemy.py`: Define a classe `Enemy`, derivada de `Character`, representando os inimigos no jogo.
- `mage.py`: Define a classe `Mage`, derivada de `Character`, representando personagens magos.
- `warrior.py`: Define a classe `Warrior`, derivada de `Character`, representando personagens guerreiros.

#### Diretório `world`
- `battleCamp.py`: Define a classe `BattleCamp`, responsável por gerenciar as batalhas entre personagens, incluindo métodos para iniciar batalhas e gerenciar ações de combate.

#### Arquivo `main.py`
- Arquivo principal que inicializa os personagens e inicia uma batalha, demonstrando a funcionalidade básica do jogo.

## Como Jogar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/RPG_textual.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd RPG_textual
    ```

3. Execute o jogo:
    ```bash
    python main.py
    ```

## Classes de Personagens

### Character
- Classe abstrata base para todos os personagens.
- Atributos:
  - `name`: Nome do personagem.
  - `race`: Raça do personagem.
  - `clss`: Classe do personagem (definida pelas subclasses).
  - `physical_damage`: Dano físico que o personagem pode causar.
  - `magical_damage`: Dano mágico que o personagem pode causar.
  - `life`: Vida do personagem.
- Métodos:
  - `show_character()`: Método abstrato para exibir informações do personagem.
  - `basic_attack(en)`: Método abstrato para realizar um ataque básico.

### Warrior
- Subclasse de `Character` representando um guerreiro.
- Atributos:
  - `physical_damage`: 15
  - `magical_damage`: 0
  - `life`: 70

### Mage
- Subclasse de `Character` representando um mago.
- Atributos:
  - `physical_damage`: 5
  - `magical_damage`: 20
  - `life`: 85

### Enemy
- Subclasse de `Character` representando um inimigo.
- Atributos:
  - `physical_damage`: 5
  - `magical_damage`: 3
  - `life`: 40

## Campo de Batalha

### BattleCamp
- Classe responsável por gerenciar as batalhas entre personagens.
- Métodos:
  - `make_scene()`: Cria o cenário de batalha e inicia a batalha.
  - `manage_battle(choice)`: Gerencia as ações de combate com base na escolha do jogador.
  - `start_battle()`: Inicia o loop de combate onde o jogador e o inimigo se revezam atacando.

## Exemplo de Saída

```plaintext
Name: Foo
Class: Warrior
Race: Human
Physical damage: 15
Magical damage: 0
Life: 70

Name: BarFoo
Class: Mage
Race: Human
Physical damage: 5
Magical damage: 20
Life: 85

Name: Baldurs
Class: Enemy
Race: Goblin
Physical damage: 5
Magical damage: 3
Life: 40

You have found an enemy!!
Your name is Baldurs
Life: 40hp

Start attacking
Which scam do you want to use?
(1)Basic_atack or (2)Nothing
=> 1

You attacked!!
Life of enemy: 20
Which scam do you want to use?
(1)Basic_atack or (2)Nothing
=> 1

You attacked!!
Baldurs died!
