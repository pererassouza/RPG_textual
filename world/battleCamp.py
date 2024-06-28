from characters import Character
from config.chat_escolha import config_choice


class BattleCamp:
    def __init__(self, ch: Character, en: Character):
        self.character = ch
        self.enemy = en

    def make_scene(self):
        print("You have found an enemy!!")
        print(f"Enemy name: {self.enemy.name}")
        print(f"Life: {self.enemy.life}hp\n")
        self.start_battle()

    def manage_battle(self, choice):
        print()
        if choice == '1':
            self.character.basic_attck(self.enemy)
            print("You attacked!!")
            if self.enemy.life <= 0:
                print(f"{self.enemy.name} died!")
                return
            print(f"Life of enemy: {self.enemy.life}")
            return

        elif choice == '2':
            self.character.intimidar(self.enemy)
            if self.enemy.resistencia <= 0:
                print("Resistencia zerada")
                return
            print("You intimidated!!")
            print(f"Resistance of enemy: {self.enemy.resistencia}")

        elif choice == '3':
            self.character.power_up()
            print("You used Power Up!!")
            print(f"Your physical damage: {self.character.physical_damage}")
            print(f"Your magical damage: {self.character.magical_damage}")

        else:
            ...

    def start_battle(self):
        print("\nStart attacking")
        while self.character.life > 0 and self.enemy.life > 0:
            print("Which attack do you want to use?")
            print("(1)Basic_attack\n(2)Intimidar\n(3)Power Up\n(4)Nothing")
            choice = input("=> ")
            self.manage_battle(choice)
            if self.enemy.life <= 0:
                break

            print("\nEnemy's attacking")

            funcoes = {
                "basic_attck": self.enemy.basic_attck,
                "intimidar": self.enemy.intimidar,
                "power_up": self.enemy.power_up
            }

            escolha_inimigo = config_choice(
                self.enemy.life, self.enemy.physical_damage,
                self.enemy.magical_damage,
                self.character.life, self.character.physical_damage,
                self.character.magical_damage,
                self.enemy.resistencia, self.character.resistencia
            )

            print(f"Enemy choice: {escolha_inimigo}")  # Debug print

            if escolha_inimigo in funcoes:
                funcoes[escolha_inimigo](self.character)

                if escolha_inimigo == "basic_attck":
                    print("Enemy Attacked!!")
                    if self.character.life <= 0:
                        print("You died!")
                        break
                    print(f"Your life: {self.character.life}")
                elif escolha_inimigo == "intimidar":
                    if self.character.resistencia <= 0:
                        print("Resistencia zerada")
                        continue
                    print("Enemy's intimidated!!")
                    print(f"Your Resistance: {self.character.resistencia}")
                elif escolha_inimigo == "power_up":
                    print("Enemy used Power Up!!")
                    print(f"Enemy physical damage: {
                          self.enemy.physical_damage}")
                    print(f"Enemy magical damage: {self.enemy.magical_damage}")
            else:
                print(f"Invalid enemy choice: {
                      escolha_inimigo}")  # Debug print
            print()
