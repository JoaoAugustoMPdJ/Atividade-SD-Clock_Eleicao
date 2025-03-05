import json

class Banco:
    def __init__(self, nome):
       
        self.nome = nome
        self.clock = 0
        self.transacoes = []  

    def evento(self, tipo, valor=None):
       
        self.clock += 1  
        log_entry = {"agencia": self.nome, "evento": tipo, "valor": valor, "clock": self.clock}
        self.transacoes.append(log_entry)  
        print(json.dumps(log_entry, indent=2)) 

    def enviar_transacao(self, destino, valor):
       
        self.clock += 1  
        print(f" {self.nome} enviou R${valor} para {destino.nome}. Clock: {self.clock}")
        destino.receber_transacao(self.clock, valor)

    def receber_transacao(self, timestamp, valor):
        
        self.clock = max(self.clock, timestamp) + 1 
        self.evento("Recebimento de Transferência", valor)  



ag1 = Banco("Agência Centro")
ag2 = Banco("Agência Norte")
ag3 = Banco("Agência Sul")


ag1.evento("Depósito", 1000)  
ag1.enviar_transacao(ag2, 500)  
ag2.enviar_transacao(ag3, 200)  
ag3.evento("Saque", 50)  
