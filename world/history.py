from config.chat import config_scene


class Cenario:
    def make_initial_history(self):
        self.cenario_atual = config_scene()
        print(self.cenario_atual, '\n')
        return self.cenario_atual
