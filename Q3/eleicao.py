import random

class Lutador:
    def __init__(self, nome):
        self.nome = nome
        self.forca = random.randint(50, 100)  # Força aleatória entre 50 e 100
        self.ativo = True

    def iniciar_eleicao(self, equipe):
        print(f"⚔️ {self.nome} iniciou uma eleição!")
        adversarios = [l for l in equipe if l.forca > self.forca and l.ativo]

        if not adversarios:
            print(f"👑 {self.nome} venceu a eleição e é o novo Capitão!")
            return

        mais_forte = max(adversarios, key=lambda l: l.forca)
        print(f"🗡️ {self.nome} desafia {mais_forte.nome}!")
        mais_forte.iniciar_eleicao(equipe)

# Criando os lutadores
equipe = [Lutador("Luffy"), Lutador("Zoro"), Lutador("Sanji")]

# Simulação de falha de Luffy
equipe[0].ativo = False
equipe[1].iniciar_eleicao(equipe)
