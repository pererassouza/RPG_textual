from config.chat import criar_história


class Cenario:
    def make_initial_history(self):
        self.cenario_atual = criar_história()
        print(self.cenario_atual, '\n')
        return self.cenario_atual
