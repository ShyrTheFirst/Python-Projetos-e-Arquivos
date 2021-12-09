import pygame, sys, random

relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
font_default = pygame.font.get_default_font()
fonte = pygame.font.SysFont(font_default, 30)
pygame.display.set_caption('Old Era')
largura = 800
meia_largura = largura//2
altura = 600
meia_altura = altura//2
tela = pygame.display.set_mode((largura,altura))
cima = False
baixo = False
direita = False
esquerda = False
virar = False
subir = False
dead = False
level = 0
pos = [0,0]
posmons = [400,300]
char = pygame.image.load('player1.png')
monster = pygame.image.load('monster.png')

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

game_on = True
while game_on == True:
   tela.fill((0,0,0))
   tela.blit(char, pos)
   tela.blit(monster,posmons)
   pygame.display.flip()
   if cima == True:
      pos[1] -= 0.3
   if baixo == True:
      pos[1] += 0.3
   if direita == True:
      pos[0] += 0.3
   if esquerda == True:
      pos[0] -= 0.3
   if pos[0] >= largura:
       pos[0] = -50
   if pos[1] >= altura:
       pos[1] = -50
   if pos[0] <= -55:
       pos[0] = largura-50
   if pos[1] <= -55:
       pos[1] = altura-50

   
   if posmons[0] >= largura-50:
       virar = True
   if posmons[1] >= altura-50:
       subir = True
   if posmons[0] <= 0:
       virar = False
   if posmons[1] <= 0:
       subir = False
   if virar == True:
       posmons[0] -= 0.3
   else:
       posmons[0] += 0.3
   if subir == True:
       posmons[1] -= 0.3
   else:
       posmons[1] += 0.3
   char_rect = char.get_rect(topleft=(pos))
   mons_rect = monster.get_rect(topleft=(posmons))
   if pygame.Rect.colliderect(char_rect,mons_rect):
       monster = pygame.image.load('monster_defeated.png')
       posmons = [-10,-10]
       
       dead = True
   else:
       pass
   if dead == True:
       levelup(1)
       
       monster = pygame.image.load('monster.png')
       posmons[0] = random.randint(0, largura-50)
       posmons[1] = random.randint(0, altura-50)
       dead = False
       
       
   
      
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            cima = True
         if event.key == pygame.K_DOWN:
            baixo = True
         if event.key == pygame.K_LEFT:
            esquerda = True
         if event.key == pygame.K_RIGHT:
            direita = True
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_UP:
            cima = False
         if event.key == pygame.K_DOWN:
            baixo = False
         if event.key == pygame.K_LEFT:
            esquerda = False
         if event.key == pygame.K_RIGHT:
            direita = False
   pygame.display.update()
