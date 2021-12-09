import hashlib

class TestBlock:
    
    def __init__(self, hash_anterior, objeto):

        self.hash_anterior = hash_anterior
        self.objeto = objeto

        self.data_bloco = f"{objeto} - {hash_anterior}"
        self.hash_bloco = hashlib.sha256(self.data_bloco.encode()).hexdigest()

class TestChain:
    def __init__(self):
        self.cadeia = []
        self.gerar_genesis()
        
    def gerar_genesis(self):
        self.cadeia.append(TestBlock("0","Cadeia de usuarios"))

    def criar_bloco(self, objeto):
        hash_anterior = self.ultimo_bloco.hash_bloco
        self.cadeia.append(TestBlock(hash_anterior, objeto))

    def mostrar_cadeia(self):
        for i in range(len(self.cadeia)):
            
            print(f"Data {i}: {self.cadeia[i].data_bloco}")
            print(f"Hash {i}: {self.cadeia[i].hash_bloco}\n")

    @property
    def ultimo_bloco(self):
        return self.cadeia[-1]


t1 = "George"
t2 = "Joe"
t3 = "Adam"
t4 = "Bob"
t5 = "Charlie"
t6 = "David"

myblockchain = TestChain()
myblockchain.criar_bloco(t1)
myblockchain.criar_bloco(t2)
myblockchain.criar_bloco(t3)
myblockchain.criar_bloco(t4)
myblockchain.criar_bloco(t5)
myblockchain.criar_bloco(t6)
myblockchain.mostrar_cadeia()
