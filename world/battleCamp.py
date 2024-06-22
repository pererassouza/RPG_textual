from characters import Character


class BattleCamp:
    def __init__(self, ch: Character, en: Character):
        self.character = ch
        self.enemy = en

    def make_scene(self):
        print("You have found an enemy!!")
        print(f"Your name is {self.enemy.name}")
        print(f"Life: {self.enemy.life}hp\n")
        self.start_battle()

    def manage_battle(self, choice):
        if choice == '1':
            self.character.basic_attck(self.enemy)
            print("You attacked!!")
            if self.enemy.life <= 0:
                print(f"{self.enemy.name} died!")
                return
            print(f"Life of enemy: {self.enemy.life}")
            return
        print("Enemy's attacking")
        self.enemy.basic_attck(self.character)
        if self.character.life <= 0:
            print("You died!")
            return
        print(f"Your life: {self.character.life}")

    def start_battle(self):
        print("Start attacking")
        while self.character.life > 0 and self.enemy.life > 0:
            print("Which scam do you want to use?")
            print("(1)Basic_atack or (2)Nothing")
            choice = input("=> ")
            print()
            self.manage_battle(choice)
