
# ** Relatório - Implementação de Algoritmos Distribuídos**  
 **Disciplina**: Sistemas Distribuídos  
 **Aluno**: João Augusto Moura Peixoto de Jesus
 **Professor**: Felipe Silva  

---

## ** Clocks e Sincronização de Tempo - Simulação de Transações Bancárias**  

### **Objetivo**  
Implementar o **Relógio de Lamport** para sincronizar eventos em um sistema bancário distribuído, garantindo que as transações sejam processadas na ordem correta.  

### **Explicação do Algoritmo**  
- Cada agência bancária possui um **relógio lógico**.  
- Quando uma transação ocorre, o relógio é incrementado.  
- Ao enviar uma transação, o timestamp da operação é anexado.  
- Ao receber uma transação, a agência ajusta seu relógio lógico.  

### **Código Implementado**  
```python
import json
import random

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clock = 0

    def evento(self, tipo, valor=None):
        self.clock += 1
        print(json.dumps({"agencia": self.nome, "evento": tipo, "valor": valor, "clock": self.clock}, indent=2))

    def enviar_transacao(self, destino, valor):
        self.clock += 1
        print(f" {self.nome} enviou R${valor} para {destino.nome}. Clock: {self.clock}")
        destino.receber_transacao(self.clock, valor)

    def receber_transacao(self, timestamp, valor):
        self.clock = max(self.clock, timestamp) + 1
        self.evento("Recebimento de Transferência", valor)

# Criando agências bancárias
bancos = [Banco("Agência Centro"), Banco("Agência Norte"), Banco("Agência Sul")]

# Simulação de transações
bancos[0].evento("Depósito", random.randint(500, 2000))
bancos[0].enviar_transacao(bancos[1], random.randint(100, 500))
bancos[1].enviar_transacao(bancos[2], random.randint(50, 300))
bancos[2].evento("Saque", random.randint(50, 500))
```

### **Conclusão**  
O sistema permite a sincronização correta das transações sem a necessidade de um relógio global, garantindo uma ordem lógica dos eventos.

---

## ** Estado Global e Captura de Estado - Processos em um Computador**  

### **Objetivo**  
Implementar o **Algoritmo de Chandy-Lamport** para capturar o estado global de processos em execução dentro de um sistema operacional.  

### **Explicação do Algoritmo**  
- Cada processo representa um **programa** em execução no computador.  
- Um dos processos inicia o snapshot.  
- Cada processo salva seu estado atual (uso de CPU e memória).  
- O snapshot pode ser usado para depuração ou recuperação do sistema.  

### **Código Implementado**  
```python
import random
import threading
import time

class Processo:
    def __init__(self, nome):
        self.nome = nome
        self.uso_cpu = random.randint(10, 90)
        self.uso_memoria = random.randint(100, 800)
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

# Criando processos
processos = [Processo("Google Chrome"), Processo("VS Code"), Processo("Spotify")]

# Simulação de captura de estado
for p in processos:
    p.capturar_estado()
```

### **Conclusão**  
A captura de estado garante que o sistema possa registrar os estados de processos sem interromper suas execuções.

---

## ** Algoritmo de Eleição - Luffy, Zoro e Sanji**  

### **Objetivo**  
Implementar o **Algoritmo de Eleição de Bully** usando personagens de One Piece para simular a escolha de um novo capitão em caso de falha do líder.  

### **Explicação do Algoritmo**  
- Cada lutador tem uma **força aleatória**.  
- Se o capitão (Luffy) for derrotado, os outros disputam o comando.  
- O mais forte assume a liderança e notifica os outros.  

### **Código Implementado**  
```python
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
            return

        mais_forte = max(adversarios, key=lambda l: l.forca)
        print(f"🗡️ {self.nome} desafia {mais_forte.nome}!")
        mais_forte.iniciar_eleicao(equipe)

# Criando os lutadores
equipe = [Lutador("Luffy"), Lutador("Zoro"), Lutador("Sanji")]

# Simulação de falha de Luffy
equipe[0].ativo = False
equipe[1].iniciar_eleicao(equipe)
```

### **Conclusão**  
O algoritmo simula uma disputa entre personagens, tornando a eleição mais dinâmica e próxima da realidade.

---

## ** Detecção de Falhas - Monitoramento de Servidores**  

### **Objetivo**  
Implementar um sistema de **heartbeat** que monitora a atividade dos servidores e detecta falhas automaticamente.  

### **Explicação do Algoritmo**  
- Cada servidor envia **sinais de vida (heartbeats)** periodicamente.  
- Se um servidor parar de responder, ele é marcado como inativo.  
- O sistema remove o servidor falho da rede.  

### **Código Implementado**  
```python
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
                    print(f" Servidor {id} está fora do ar!")
                    del self.servidores[id]
            time.sleep(3)

class Servidor:
    def __init__(self, id):
        self.id = id
        self.online = True  

    def enviar_heartbeat(self, monitoramento):
        while self.online:
            print(f" Servidor {self.id} está ativo")
            time.sleep(2)

    def esta_online(self):
        return self.online

monitor = Monitoramento()
servidores = [Servidor(1), Servidor(2)]

for s in servidores:
    monitor.registrar(s)

threading.Thread(target=monitor.verificar_servidores).start()
for s in servidores:
    threading.Thread(target=s.enviar_heartbeat, args=(monitor,)).start()

time.sleep(6)
servidores[1].online = False  # Simula falha
```

### **Conclusão**  
O monitoramento automático permite detectar falhas em tempo real, garantindo a estabilidade do sistema.

---

## ** Conclusão Geral**  
A cada implementação apresentei um **cenário realista**, pois assim achei mais fácil de interpretar os conceitos propostos; Utilizando **valores aleatórios** e **mensagens descritivas** para tornar o código mais compreensivel.
