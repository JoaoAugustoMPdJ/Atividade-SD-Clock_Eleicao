import random
import threading
import time

class Processo:
    def __init__(self, nome):
        self.nome = nome
        self.uso_cpu = random.randint(10, 90)  # Simulando carga da CPU
        self.uso_memoria = random.randint(100, 800)  # Simulando uso de RAM em MB
        self.marcador_recebido = False

    def capturar_estado(self):
        if not self.marcador_recebido:
            print(f" {self.nome} salvou estado: CPU {self.uso_cpu}%, RAM {self.uso_memoria}MB")
            self.marcador_recebido = True

    def executar(self):
        while True:
            self.uso_cpu = random.randint(10, 90)
            self.uso_memoria = random.randint(100, 800)
            time.sleep(3)

p1 = Processo("Google Chrome")
p2 = Processo("Visual Studio Code")
p3 = Processo("Spotify")

p1.capturar_estado()
p2.capturar_estado()
p3.capturar_estado()

threading.Thread(target=p1.executar).start()
threading.Thread(target=p2.executar).start()
threading.Thread(target=p3.executar).start()
