import random

class Lutador:
    def __init__(self, nome):
        self.nome = nome
        self.forca = random.randint(50, 100) 
        self.ativo = True

    def iniciar_eleicao(self, equipe):
    
        print(f" {self.nome} iniciou uma eleição!")
        adversarios = [l for l in equipe if l.forca > self.forca and l.ativo]

        if not adversarios:
            print(f" {self.nome} venceu a eleição e é o novo Capitão!")
            return self

        mais_forte = max(adversarios, key=lambda l: l.forca)
        print(f" {self.nome} desafia {mais_forte.nome}!")
        return mais_forte.iniciar_eleicao(equipe)

def simular_falha_lider(equipe):
   
    lider = equipe[0]
    lider.ativo = False
    print(f"] {lider.nome} falhou e não está mais ativo!")

def encontrar_novo_lider(equipe):
  
    for lutador in equipe:
        if lutador.ativo:
            novo_lider = lutador.iniciar_eleicao(equipe)
            if novo_lider:
                return novo_lider
    return None

equipe = [Lutador("Luffy"), Lutador("Zoro"), Lutador("Sanji"), Lutador("Nami"), Lutador("Jimbe"), Lutador("Franky"), Lutador("Brook"), Lutador("Chopper"), Lutador("Robin")]

print("Força inicial dos lutadores:")
for lutador in equipe:
    print(f"{lutador.nome}: {lutador.forca}")

simular_falha_lider(equipe)

novo_lider = encontrar_novo_lider(equipe)

if novo_lider:
    print(f" O novo líder da equipe é {novo_lider.nome} com {novo_lider.forca} de força!")
else:
    print(" Não há líderes ativos na equipe.")