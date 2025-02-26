import time
import threading

class Monitoramento:
    def __init__(self):
        self.servidores = {}

    def registrar(self, servidor):
        self.servidores[servidor.id] = servidor

    def verificar_servidores(self):
        while True:
            for id, servidor in list(self.servidores.items()):
                if not servidor.esta_online():
                    print(f"⚠️ Servidor {id} está fora do ar!")
                    del self.servidores[id]
            time.sleep(3)

class Servidor:
    def __init__(self, id):
        self.id = id
        self.online = True  

    def enviar_heartbeat(self, monitoramento):
        while self.online:
            print(f"✔️ Servidor {self.id} está ativo")
            time.sleep(2)

    def esta_online(self):
        return self.online

monitor = Monitoramento()
srv1 = Servidor(1)
srv2 = Servidor(2)

monitor.registrar(srv1)
monitor.registrar(srv2)

thread_monitor = threading.Thread(target=monitor.verificar_servidores)
thread_srv1 = threading.Thread(target=srv1.enviar_heartbeat, args=(monitor,))
thread_srv2 = threading.Thread(target=srv2.enviar_heartbeat, args=(monitor,))

thread_monitor.start()
thread_srv1.start()
thread_srv2.start()

time.sleep(6)
srv2.online = False  # Simula falha no servidor 2
