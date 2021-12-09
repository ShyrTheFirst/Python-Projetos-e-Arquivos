#variaveis globais#
pontos = 10

NomePersonagem = input("Dê um nome para seu personagem: ")

class Personagem():
    Nome = NomePersonagem
    HP = 10
    FORCA = 0
    LVL = 1
    XP = 0
    Poder = 0
    Defesa = 0
    Classe = " "
    
    ####Definindo a HP do personagem####    
    def DefinirHP(self,x):
        self.HP += x
        
    ####Definindo a FORÇA do personagem####    
    def DefinirFORCA(self,y):
        self.FORCA += y
        
    ####Definindo stats após LVL UP do personagem####    
    def LVLUP(self):
        if self.LVL%5 == 0:
            self.HP += 2
            self.FORCA += 2
            
        else:
            self.HP += 1
            self.FORCA += 1
            
    ####Definindo o LVL UP do personagem####        
    def DefinirLVL(self,XP):
        if self.XP >= 100:
            print("LVL UP!")
            self.LVL += 1
            self.LVLUP()
        else:
            pass
            
    ####Definindo Poder do personagem####
    ####Com base na Força e no HP####
    def DefinirPoder(self):
        self.Poder = (self.FORCA*5)/self.HP
        
    ####Mostra o Poder do personagem####    
    def MostrarPoder(self):
        print(self.Poder)
        
    ####Definindo a Defesa do personagem####
    ####Com base no HP####
    def DefinirDefesa(self):
        self.Defesa = (self.HP*2)/10
        
    ####Mostra a Defesa do personagem####    
    def MostrarDefesa(self):
        print(self.Defesa)
        
    ####Define o Dano do personagem####
    ####O dano só é possível após declarar o inimigo####
    ####target = nome definido para a classe inimigo####
    def Dano(self, target):
        global dano_realizado
        dano_realizado = self.Poder - target.Defesa
        print(dano_realizado)
        
    ####Definindo a Classe do personagem####
    ####Escolher entre 3, Mago, Arqueiro e Guerreiro####
    def DefinirClasse(self):
        print("Escolha uma classe: Mago, Arqueiro, Guerreiro.")
        escolhendo = True
        while escolhendo:
            classe_definida = input("Digite sua escolha: ")
            if classe_definida != "Mago" and classe_definida != "Arqueiro" and classe_definida != "Guerreiro":
                print("Escolha uma classe válida!")
            else:
                escolhendo = False
        self.Classe = classe_definida
        print("A Classe escolhida foi: ", self.Classe)
        
    ####Definindo a Morte do personagem####    
    def Morte(self):
        print("Você morreu")
    
class Mago(Personagem):
    pass
class Arqueiro(Personagem):
    pass
class Guerreiro(Personagem):
    pass

        
initializing = True

while initializing:
    ##Define o nome do personagem como classe##
    NomePersonagem = Personagem()
    
    ##Escolhendo a classe do personagem##
    NomePersonagem.DefinirClasse()
    
    ##Define o LVL inicial do personagem##
    NomePersonagem.DefinirLVL(NomePersonagem.XP)
    
    ##variaveis para definir HP e força##
    pontos_para_gastar = True
    while pontos_para_gastar:
        print("Vamos definir seus atributos. Você tem: ", pontos, " disponíveis para gastar")
        escolha_att = input("Qual atributo deseja evoluir? Digite 'HP' ou 'FOR': ")
        if (escolha_att == "HP"):
            gastando_HP = int(input("Quantos pontos deseja gastar? "))
            if gastando_HP > pontos:
                print("Escolha um valor menor")
            else:
                pontos -= gastando_HP
                NomePersonagem.DefinirHP(gastando_HP)
        elif (escolha_att == "FOR"):
            gastando_FOR = int(input("Quantos pontos deseja gastar? "))
            if gastando_FOR > pontos:
                print("Escolha um valor menor")
            else:
                pontos -= gastando_FOR
                NomePersonagem.DefinirFORCA(gastando_FOR)
        else:
            print("digite 'HP' ou 'FOR'")
        if pontos == 0:
            print("Você gastou todos os pontos!")
            pontos_para_gastar = False
        else:
            pass
    ##fim das variaveis de HP e força##

    ##Definindo dados dependentes do HP e Força##
    NomePersonagem.DefinirPoder()
    NomePersonagem.DefinirDefesa()



    
    
    initializing = False
