import pygame, sys, random

##inicializando pygame##
relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
font_default = pygame.font.get_default_font()
fonte = pygame.font.SysFont(font_default, 30)
pygame.display.set_caption('GameClickerDev')
largura = 800
altura = 600
tela = pygame.display.set_mode((largura,altura))
tela.fill((0,0,0))
cor_ativa = (0,0,255)
cor_passiva = (255,0,0)
cor = cor_passiva
cor_chao = (0,66,37)
posx = 350
posy = 350
ativo = False
game_on = True
display_class = False
novo_mob = False
game_level = 1
input_usuario = " "
##fim da inicialização do pygame##

#####CLASSES#####

##Classe ITEM##
class Item():
    def __init__(self):
        self.poder = 0
        self.comprar_reta = pygame.Rect(posx+250,posy+150,50,20)
        
    def melhorar_item(self,player):
        self.poder += 1
        player.aumentar_dano()

    def atualizar_item(self,player):
        player.aumentar_dano()

    def gerar_item(self,player):
        self.item_name = 'Gerar nome pro item com rand'
        ### Gerar nome pro item: 1.escolher o tipo (espada, arco, cajado...) 2. Definir imagem através do tipo 3. Escolher quant de nomes do item 4. escolher aleatóriamente de um banco de palavras o nome do item
        
        prob_poder = random.randrange(1,100)
        self.poder += prob_poder
        self.atualizar_item(player)
        
    def botao_comprar(self):
        self.color = cor_ativa
        self.reta_botao = self.comprar_reta
        pygame.draw.rect(tela,self.color, self.reta_botao)
        pygame.display.flip()

    def comprando(self,player):
        self.color = cor_passiva
        pygame.draw.rect(tela,self.color, self.reta_botao)
        pygame.display.flip()
        pygame.time.delay(200)
        self.gerar_item(player)

##Fim Classe ITEM##

##Classe PERSONAGEM##
class Personagem():
   def __init__(self,item):
       self.level = game_level
       self.dano_normal = 1
       self.dano_arma = 0 + item.poder
       self.dano_total = self.dano_normal+self.dano_arma

   def levelup(self):
       self.level = game_level

   def aumentar_dano(self):
       self.dano_arma = 0 + item.poder
       self.dano_total = self.dano_normal + self.dano_arma
       
   def mostrar_level(self):   
       self.mostrarlevelvar = "Você está no level: %s" %(self.level)
       self.mostrarlevel = fonte.render(self.mostrarlevelvar, 1, (255,255,255))
       tela.blit(self.mostrarlevel, (30,55))
       
   def limpar_level(self):        
       sizex,sizey = pygame.font.Font.size(fonte,self.mostrarlevelvar)
       limpar_rect = pygame.Rect(30,55,sizex,sizey)
       pygame.draw.rect(tela,(0,0,0),limpar_rect)

   def name(self, name):
      name = str(name)
      mostrar_nome = fonte.render(name, 1, (255,255,255))
      tela.blit(mostrar_nome, (30,30))

##Fim Classe PERSONAGEM##

##Classe MONSTRO##
class Monstro():
   def __init__(self, cor_ativa, dificuldade):
        rect = pygame.Rect(posx,posy,50,50)
        self.color = cor_ativa
        self.dificuldade = dificuldade
        self.set_vida = int(self.dificuldade*10)
       
   def desenhar(self):
      self.color = cor_ativa
      self.rect = pygame.Rect(posx,posy,50,50)
      pygame.draw.rect(tela,self.color, self.rect)
      pygame.display.flip()
      
   def vida(self):
       self.mostrar_vida = "Vida: %i" %(self.set_vida)
       self.mostrar_vida_render = fonte.render(self.mostrar_vida, 1, (255,255,255))
       tela.blit(self.mostrar_vida_render, (posx-10,posy+70))
      
   def clicou(self,player):
      self.color = cor_passiva
      dano_total = player.dano_total
      self.set_vida -= dano_total
      self.rect = pygame.Rect(posx,posy,50,50)
      pygame.draw.rect(tela,self.color, self.rect)
      pygame.display.flip()
      pygame.time.delay(200)
      if self.set_vida <= 0:
          self.morte(player)
      else:
          self.vida()
      

   def morte(self,player):
       global game_level, novo_mob
       game_level += 1
       player.levelup()
       novo_mob = True

##Fim Classe MONSTRO##

##Classe CHAO##
class chao():
    def __init__(self):
        self.posx = 0
        self.posy = 410
        self.rect = pygame.Rect(self.posx,self.posy,800,600)

    def desenhar(self):
        self.color = cor_chao
        pygame.draw.rect(tela,self.color,self.rect)

##Fim Classe CHAO##

#####INICIO DO CODIGO DO JOGO#####
nome = fonte.render("Escolha seu nome: ", 1, (255,255,255))
tela.blit(nome, (80,80))
pygame.display.update()

###DEFINIR NOME POR INPUT###
while game_on == True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
         
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RETURN:
            display_class = True
            tela.fill((0,0,0))
            game_on = False
         if event.key == pygame.K_BACKSPACE:
            input_usuario = input_usuario[:-1]
            tela.fill((0,0,0))
            tela.blit(nome, (80,80))
            pygame.display.flip()
         else:
            input_usuario += event.unicode
             
   mostrar_texto = fonte.render(input_usuario, 1, (255,255,255))
   tela.blit(mostrar_texto,(100,100))
   pygame.display.update()
###FIM DA DEFINIÇÃO POR INPUT###
   
###LIMPANDO A TELA E FAZENDO AJUSTES###
tela.fill((0,0,0))
pygame.display.update()
input_usuario = input_usuario[:-1]

###DEFININDO AS CLASSES###
item = Item()
char = Personagem(item)
chao = chao()
char.mostrar_level()
char.name(input_usuario)
monstro = Monstro(cor,game_level)

while display_class == True:
    if novo_mob:
        monstro = Monstro(cor,game_level)
        novo_mob = False
    else:
        monstro.desenhar()
        chao.desenhar()
        monstro.vida()
        item.botao_comprar()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mouse.get_pressed() == (1,0,0):
            posicao_mouse = pygame.mouse.get_pos()
            RETA = monstro.rect
            botao_comprar = item.comprar_reta
            if pygame.Rect.collidepoint(RETA,posicao_mouse):
                monstro.clicou(char)
                char.limpar_level()
                char.mostrar_level()
                pygame.display.flip()
            if pygame.Rect.collidepoint(botao_comprar,posicao_mouse):
                item.comprando(char)
