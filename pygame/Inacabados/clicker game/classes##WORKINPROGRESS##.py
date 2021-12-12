import pygame,sys,random
from vars import sair_do_jogo
import vars as v
from escrita_por_letra import escrever_por_letra as escrever

pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((v.largura,v.altura))
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)




#####CLASSES#####

##Classe BOTAO##
class Botao():
    def __init__(self,x,y,imagem, imagem_press, imagem_emcima):
        self.imagem = imagem
        self.imagem_pressionado = imagem_press
        self.imagem_emcima = imagem_emcima
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)

    def desenhar(self,tela):
        tela.blit(self.imagem,(self.rect.x,self.rect.y))
    def desenhar_clique(self,tela):
        tela.blit(self.imagem_pressionado,(self.rect.x,self.rect.y))
    def desenhar_emcima(self,tela):
        tela.blit(self.imagem_emcima,(self.rect.x,self.rect.y))
        
##Fim Classe BOTAO##
        
##Classe ITEM##
class Item():
    def __init__(self):
        self.poder = 0
        self.comprar_reta = pygame.Rect(v.posx+250,v.posy+150,50,20)
        self.melhorar_reta = pygame.Rect(v.posx+250,v.posy+120,50,20)
        self.aumento_poder = 0
        
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
        ### blitar item, poder do item e bonus(melhorar)###
        self.atualizar_item(player)
        
    def botao_comprar(self):
        self.color = v.cor_ativa
        self.reta_botao = self.comprar_reta
        pygame.draw.rect(tela,self.color, self.reta_botao)

    def comprando(self,player):
        self.color = v.cor_passiva
        pygame.draw.rect(tela,self.color, self.reta_botao)
        pygame.display.flip()
        pygame.time.delay(200)
        self.gerar_item(player)

    def botao_melhorar(self):
        self.color = v.cor_ativa
        self.reta_botao_melhorar = self.melhorar_reta
        pygame.draw.rect(tela,self.color, self.reta_botao_melhorar)

    def melhorando(self,player):
        self.color = v.cor_passiva
        pygame.draw.rect(tela,self.color, self.reta_botao_melhorar)
        pygame.display.flip()
        pygame.time.delay(200)
        self.aumento_poder += 1
        self.melhorar_item(player)
        self.atualizar_item(player)

##Fim Classe ITEM##

##Classe PERSONAGEM##
class Personagem():
   def __init__(self,item):
       self.level = v.game_level
       self.dano_normal = 1
       self.dano_arma = 0 + item.poder
       self.dano_total = self.dano_normal+self.dano_arma

   def levelup(self):
       self.level = v.game_level

   def aumentar_dano(self):
       self.dano_arma = 0 + item.poder
       self.dano_total = self.dano_normal + self.dano_arma
       
   def mostrar_level(self):   
       self.mostrarlevelvar = "Voce esta no level: %s" %(self.level)
       self.mostrarlevel = fonte.render(self.mostrarlevelvar, 1, (255,255,255))
       tela.blit(self.mostrarlevel, (30,55))
       
   def limpar_level(self):        
       sizex,sizey = pygame.font.Font.size(fonte,self.mostrarlevelvar)
       limpar_rect = pygame.Rect(30,55,sizex,sizey)
       pygame.draw.rect(tela,(0,0,0),limpar_rect)

   def mostrar_dano(self):   
       self.mostrardanovar = "Seu dano e: %s" %(self.dano_total)
       self.mostrardano = fonte.render(self.mostrardanovar, 1, (255,255,255))
       tela.blit(self.mostrardano, (30,85))
       
   def limpar_dano(self):        
       sizex_dano,sizey_dano = pygame.font.Font.size(fonte,self.mostrardanovar)
       limpar_dano_rect = pygame.Rect(30,85,sizex_dano,sizey_dano)
       pygame.draw.rect(tela,(0,0,0),limpar_dano_rect)

   def name(self, name):
      name = str(name)
      mostrar_nome = fonte.render(name, 1, (255,255,255))
      tela.blit(mostrar_nome, (30,30))

##Fim Classe PERSONAGEM##

##Classe MONSTRO##
class Monstro():
   def __init__(self, cor_ativa, dificuldade):
        rect = pygame.Rect(v.posx,v.posy,50,50)
        self.color = cor_ativa
        self.dificuldade = dificuldade
        self.set_vida = int(self.dificuldade*10)
       
   def desenhar(self):
      self.color = v.cor_ativa
      self.rect = pygame.Rect(v.posx,v.posy,50,50)
      pygame.draw.rect(tela,self.color, self.rect)
      pygame.display.flip()
      
   def vida(self):
       self.mostrar_vida = "Vida: %i" %(self.set_vida)
       self.mostrar_vida_render = fonte.render(self.mostrar_vida, 1, (255,255,255))
       tela.blit(self.mostrar_vida_render, (v.posx-10,v.posy+70))
      
   def clicou(self,player):
      self.color = v.cor_passiva
      dano_total = player.dano_total
      self.set_vida -= dano_total
      self.rect = pygame.Rect(v.posx,v.posy,50,50)
      pygame.draw.rect(tela,self.color, self.rect)
      pygame.display.flip()
      pygame.time.delay(200)
      if self.set_vida <= 0:
          self.morte(player)
      else:
          self.vida()
      

   def morte(self,player):
       v.game_level += 1
       player.levelup()
       v.novo_mob = True

##Fim Classe MONSTRO##

##Classe CHAO##
class chao():
    def __init__(self):
        self.posx = 0
        self.posy = 410
        self.rect = pygame.Rect(self.posx,self.posy,800,600)

    def desenhar(self):
        self.color = v.cor_chao
        pygame.draw.rect(tela,self.color,self.rect)

##Fim Classe CHAO##
