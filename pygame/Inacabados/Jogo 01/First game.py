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
#Define the Buttons 
 retStart = pygame.Rect(50,270,100,30)
 retExit = pygame.Rect(50,390,100,30)
#Define the screen and screen color
 tela = pygame.display.set_mode([800, 600])
 tela.fill((10,10,10))
#draw rect of buttons
 pygame.draw.rect(tela,(27,109,37), retStart) 
 pygame.draw.rect(tela,(27,109,37), retExit)
#update screen
 pygame.display.update()
#detect if rect is being pressed
 if pygame.mouse.get_pressed() == (1,0,0):
             mouseposition = pygame.mouse.get_pos()
             if retStart.collidepoint(mouseposition):
              print("Let's Start")
              niveis()
             if retExit.collidepoint(mouseposition):
              print("We are leaving now?")
              pygame.quit()
             
#pra lembrar sobre rect: (horizontal lugar, vertical lugar, horizontal tamanho, vertical tamanho)
def niveis():
    Endgame = False
    tela = pygame.display.set_mode([1024, 768])
    frames = pygame.time.Clock()
    azul_fundo = (51,216,230)
    verde_ganhou = (120,218,122)
    vermelho_perdeu = (193,30,30)
    verde_grama = (23,115,30)
    
    lvl01 = False
    if lvl01 == False:
     retSelf = pygame.Rect(10,10,25,25)
     #Lose game rect
     ret1Lose = pygame.Rect(10,40,980,5)
     ret2Lose = pygame.Rect(35,100,980,5)
     ret3Lose = pygame.Rect(10,200,980,5)
     ret4Lose = pygame.Rect(35,300,980,5)
     ret5Lose = pygame.Rect(10,400,980,5)
     #Win game rect
     retWin = pygame.Rect(0,750,1024,10)
     
     while lvl01 == False: 
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
              retSelf = retSelf.move(0,-10)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
              retSelf = retSelf.move(0,10)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
              retSelf = retSelf.move(10,0)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
              retSelf = retSelf.move(-10,0)
      frames.tick(120)
      tela.fill(azul_fundo)
      pygame.draw.rect(tela,(120,22,110), retSelf)
      pygame.draw.rect(tela,(235,11,0), ret1Lose)
      pygame.draw.rect(tela,(235,11,0), ret2Lose)
      pygame.draw.rect(tela,(235,11,0), ret3Lose)
      pygame.draw.rect(tela,(235,11,0), ret4Lose)
      pygame.draw.rect(tela,(235,11,0), ret5Lose)
      pygame.draw.rect(tela,(0,128,0), retWin)
      pygame.display.update()
      if pygame.Rect.colliderect(retSelf, ret1Lose):
            print("You Collide!")
            lvl01 = True
            lvl02 = True
            Endgame = True
            break
      if pygame.Rect.colliderect(retSelf, ret2Lose):
            print("You Collide!")
            lvl01 = True
            lvl02 = True
            Endgame = True
            break
      if pygame.Rect.colliderect(retSelf, ret3Lose):
            print("You Collide!")
            lvl01 = True
            lvl02 = True
            Endgame = True
            break
      if pygame.Rect.colliderect(retSelf, ret4Lose):
            print("You Collide!")
            lvl01 = True
            lvl02 = True
            Endgame = True
            break
      if pygame.Rect.colliderect(retSelf, ret5Lose):
            print("You Collide!")
            lvl01 = True
            lvl02 = True
            Endgame = True
            break
      if pygame.Rect.colliderect(retSelf, retWin):
            print("You passed!")
            lvl01 = True
            lvl02 = False
            break
     if lvl02 == False:
      retSelf = pygame.Rect(22,33,20,20)
      ret2 = pygame.Rect(200,150,400,300)
      #Win game rect
      ret3 = pygame.Rect(0,750,1024,10)
     while lvl02 != True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
              retSelf = retSelf.move(0,-5)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
              retSelf = retSelf.move(0,5)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
              retSelf = retSelf.move(5,0)
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
              retSelf = retSelf.move(-5,0)
      frames.tick(120)
      tela.fill(azul_fundo)
      pygame.draw.rect(tela,(120,22,110), retSelf)
      pygame.draw.rect(tela,(235,11,0), ret2)
      pygame.draw.rect(tela,(0,128,0), ret3)

      pygame.display.update()
      if pygame.Rect.colliderect(retSelf, ret2):
            print("You Collide!")
            lvl02 = True
            lvl01 = True
            Endgame = True
            
      if pygame.Rect.colliderect(retSelf, ret3):
            print("You passed!")
            lvl02 = True
            
      if Endgame == True:
        startmenu()




main()
