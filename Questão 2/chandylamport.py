import random
import threading
import time

class Processo:
    def __init__(self, nome):
        
        self.nome = nome
        self.uso_cpu = random.randint(10, 90)  
        self.uso_memoria = random.randint(100, 800)  
        self.marcador_recebido = False 
        self.fila_mensagens = []  
        self.vizinhos = []  

    def conectar(self, *processos):
        
        self.vizinhos.extend(processos)

    def capturar_estado(self):
       
        if not self.marcador_recebido:
            print(f" {self.nome} salvou estado: CPU {self.uso_cpu}%, RAM {self.uso_memoria}MB")
            self.marcador_recebido = True  

            for processo in self.vizinhos:
                processo.receber_marcador()

    def receber_marcador(self):
      
        if not self.marcador_recebido:
            self.capturar_estado()

    def enviar_mensagem(self, destino, mensagem):
      
        print(f" {self.nome} enviou mensagem para {destino.nome}: {mensagem}")
        destino.receber_mensagem(self.nome, mensagem)

    def receber_mensagem(self, origem, mensagem):
       
        if self.marcador_recebido:
            self.fila_mensagens.append((origem, mensagem))
        print(f" {self.nome} recebeu mensagem de {origem}: {mensagem}")

    def executar(self):
      
        while True:
            self.uso_cpu = random.randint(10, 90) 
            self.uso_memoria = random.randint(100, 800)  
            time.sleep(3) 

p1 = Processo("Google Chrome")
p2 = Processo("Visual Studio Code")
p3 = Processo("Spotify")

p1.conectar(p2, p3)
p2.conectar(p3)

print("\n Iniciando Captura de Estado pelo Google Chrome ")
p1.capturar_estado()

time.sleep(2)
p2.enviar_mensagem(p3, "Atualização de arquivo salva.")
p3.enviar_mensagem(p1, "Música carregada com sucesso.")

threading.Thread(target=p1.executar).start()
threading.Thread(target=p2.executar).start()
threading.Thread(target=p3.executar).start()
