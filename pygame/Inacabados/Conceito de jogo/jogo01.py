class Player:
    def __init__(self,nome,confederacao,linhagem):
        self.nome = nome
        self.confederacao = confederacao
        self.linhagem = linhagem
        self.level = 1
        self.exp = 0
        self.att = 0
        print("Bem vindo ao jogo %s, da confederacao dos %ss e da linhagem %s" %(nome,confederacao,linhagem))

        self.arqueiro = False
        self.mago = False
        self.guerreiro = False
        if confederacao == "mago":
            self.mago = True            
        if confederacao == "guerreiro":
            self.guerreiro = True
        if confederacao == "arqueiro":
            self.arqueiro = True

        if self.mago:
            self.STR = 1
            self.AGI = 1
            self.WIS = 3
            self.HP = 80
            self.MP = 80
        if self.arqueiro:
            self.STR = 1
            self.AGI = 3
            self.WIS = 1
            self.HP = 100
            self.MP = 50
        if self.guerreiro:
            self.STR = 3
            self.AGI = 1
            self.WIS = 1
            self.HP = 150
            self.MP = 20



    def atributos(self,linhagem):
        if self.linhagem == "humano":
            print("voce e um humano!")
        if self.linhagem == "elfo":
            print("voce e um elfo")
        if self.linhagem == "anão":
            print("voce e um anão")

    def expgain(self,exp):
        ##a cada 500 de xp, upa 1 level!##
        self.exp += exp
        if self.exp == 500:
            self.levelup(1)

    def levelup(self,up):
        self.level += up
        self.att += 5*up
        if self.mago:
            self.STR += 1*up
            self.AGI += 1*up
            self.WIS += 3*up
            self.HP += 5*up
            self.MP += 15*up
        if self.arqueiro:
            self.STR += 1*up
            self.AGI += 3*up
            self.WIS += 1*up
            self.HP += 10*up
            self.MP += 10*up
        if self.guerreiro:
            self.STR += 3*up
            self.AGI += 1*up
            self.WIS += 1*up
            self.HP += 15*up
            self.MP += 5*up
        self.exp = 0
            

class Mob:
    def __init__(self,nome,tipo,level):
        self.nome = nome
        self.tipo = tipo
        self.level = level
        
    def morte(self,player):
        monster_exp = int(self.level*10)
        player.expgain(monster_exp)
        

        


nome = input("Insira seu nome: ")
confederacao = input("Insira a confederação que faz parte: (mago,guerreiro,arqueiro) ")
linhagem = input("Insira a linhagem que faz parte: (humano,elfo,anão) ")
confederacao = confederacao.lower()
linhagem = linhagem.lower()
player = Player(nome,confederacao,linhagem)

player.atributos(linhagem)
print("level", player.level)
print("STR", player.STR)
print("AGI", player.AGI)
print("WIS", player.WIS)
print("HP", player.HP)
print("MP", player.MP)
print("att", player.att)

player.expgain(500)
print("after lvl up")
print("STR", player.STR)
print("AGI", player.AGI)
print("WIS", player.WIS)
print("HP", player.HP)
print("MP", player.MP)
print("att", player.att)
print("level", player.level)

mob1 = Mob("serpente","voador",10)

mob1.morte(player)
print("after lvl up from mob")
print("STR", player.STR)
print("AGI", player.AGI)
print("WIS", player.WIS)
print("HP", player.HP)
print("MP", player.MP)
print("att", player.att)
print("level", player.level)




        
