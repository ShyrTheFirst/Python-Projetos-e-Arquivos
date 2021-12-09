import pygame, sys, random

relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
font_default = pygame.font.get_default_font()
fonte = pygame.font.SysFont(font_default, 30)
pygame.display.set_caption('Test Game about class')
largura = 800
altura = 600
meia_altura = altura//2
meia_largura = largura//2
tela = pygame.display.set_mode((largura,altura))
tela.fill((0,0,0))
level = 0
cor_ativa = (0,0,255)
cor_passiva = (255,0,0)
cor = cor_passiva
posx = 100
posy = 100
ativo = False
game_on = True
display_class = False
input_usuario = " "

class Personagem():
   
   classe = "Guerreiro"
   raca = "Humano"
   global level
   level = 1

   def levelup(int):
       global level
       level += 1
       subirlevel = fonte.render("Você evoluiu 1 lvl", 1, (255,255,255))
       tela.blit(subirlevel, (meia_largura, meia_altura))
       mostrarlevelvar = "Seu nivel é: %s" %(level)
       mostrarlevel = fonte.render(mostrarlevelvar, 1, (255,255,255))
       tela.blit(mostrarlevel, (meia_largura+50, meia_altura+50))
       pygame.display.flip()
       pygame.time.delay(500)

   def name(self, name):
      name = str(name)
      mostrar_nome = fonte.render(name, 1, (255,255,255))
      tela.blit(mostrar_nome, (300,300))
      pygame.display.update()

      
class monster():
   global posx,posy,cor
   rect = pygame.Rect(posx,posy,50,50)
   color = cor_ativa
       
   def desenhar(self):
      self.color = cor_ativa
      self.rect = pygame.Rect(posx,posy,50,50)
      pygame.draw.rect(tela,self.color, self.rect)
      pygame.display.flip()
   def mover(self):
      global posx,posy
      self.color = cor_passiva
      posx = random.randint(0,largura-100)
      posy = random.randint(0,altura-100)
      self.desenhar(monster)
      pygame.display.update()
   def clicou(self):
      self.color = cor_passiva
      self.rect = pygame.Rect(posx,posy,50,50)
      pygame.draw.rect(tela,self.color, self.rect)
      pygame.display.flip()
      pygame.time.delay(200)
      
      
        
nome = fonte.render("Escolha seu nome: ", 1, (255,255,255))
tela.blit(nome, (250,250))
pygame.display.update()

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
            tela.blit(nome, (250,250))
            pygame.display.flip()
         else:
            input_usuario += event.unicode
         
   mostrar_texto = fonte.render(input_usuario, 1, (255,255,255))
   tela.blit(mostrar_texto,(300,300))
   pygame.display.update()
tela.fill((0,0,0))
pygame.display.update()
input_usuario = input_usuario[:-1]
while display_class == True:
   monster.desenhar(monster)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
   if pygame.mouse.get_pressed() == (1,0,0):
      posicao_mouse = pygame.mouse.get_pos()
      RETA = monster.rect
      if pygame.Rect.collidepoint(RETA,posicao_mouse):
         monster.clicou(monster)
         char.levelup()
         monster.mover(monster)
         tela.fill((0,0,0))
         pygame.display.update()

    
   char = Personagem()
   char.name(input_usuario)
