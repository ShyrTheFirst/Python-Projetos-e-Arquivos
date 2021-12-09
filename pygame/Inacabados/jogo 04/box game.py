import pygame

def main():
    pygame.init()
    tela = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Primeiro Jogo")
    frames = pygame.time.Clock()

    sair = False
    while sair != True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sair = True
         else:
             startmenu()
    pygame.quit()

def startmenu():
#Define the rect
 retStart = pygame.Rect(400,300,100,30)
#Define the screen and screen color
 tela = pygame.display.set_mode([800, 600])
 tela.fill((10,10,10))
#draw rect
 pygame.draw.rect(tela,(120,22,110), retStart)
#update screen
 pygame.display.update()
#detect if rect is being pressed
 if pygame.mouse.get_pressed() == (1,0,0):
             mouseposition = pygame.mouse.get_pos()
             if retStart.collidepoint(mouseposition):
              print("Let's Start")
              niveis()
             else:
              pass

def niveis():
    Endgame = False
    tela = pygame.display.set_mode([800, 600])
    frames = pygame.time.Clock()
    vermelho_vinho = (94,33,41)
    
    lvl01 = False
    if lvl01 == False:
     ret1 = pygame.Rect(10,10,20,20)
     ret2 = pygame.Rect(200,150,400,300)
     ret3 = pygame.Rect(100,100,10,10)
     
     while lvl01 == False: 
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sair = True
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
              ret1 = ret1.move(0,-5)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
              ret1 = ret1.move(0,5)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
              ret1 = ret1.move(5,0)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
              ret1 = ret1.move(-5,0)
      frames.tick(30)
      tela.fill(vermelho_vinho)
      pygame.draw.rect(tela,(120,22,110), ret1)
      pygame.draw.rect(tela,(235,11,0), ret2)
      pygame.draw.rect(tela,(0,128,0), ret3)
      pygame.display.update()
      if pygame.Rect.colliderect(ret1, ret2):
            print("You Collide!")
            lvl01 = True
            lvl02 = True
            Endgame = True
            break
      if pygame.Rect.colliderect(ret1, ret3):
            print("You passed!")
            lvl01 = True
            lvl02 = False
            break
     if lvl02 == False:
      ret1 = pygame.Rect(22,33,20,20)
      ret2 = pygame.Rect(200,150,400,300)
      ret3 = pygame.Rect(132,321,10,10)
     while lvl02 != True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sair = True
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
              ret1 = ret1.move(0,-5)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
              ret1 = ret1.move(0,5)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
              ret1 = ret1.move(5,0)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
              ret1 = ret1.move(-5,0)
      frames.tick(30)
      tela.fill(vermelho_vinho)
      pygame.draw.rect(tela,(120,22,110), ret1)
      pygame.draw.rect(tela,(235,11,0), ret2)
      pygame.draw.rect(tela,(0,128,0), ret3)

      pygame.display.update()
      if pygame.Rect.colliderect(ret1, ret2):
            print("You Collide!")
            lvl02 = True
            lvl01 = True
            Endgame = True
            
      if pygame.Rect.colliderect(ret1, ret3):
            print("You passed!")
            lvl02 = True
            
      if Endgame == True:
        startmenu()




main()
