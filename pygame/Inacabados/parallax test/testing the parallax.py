import pygame

WIDTH = 800
HEIGHT = 400
pygame.init()
tela = pygame.display.set_mode([WIDTH, HEIGHT])
frames = pygame.time.Clock()
posx = 0
posy = 0

#creating back
layer_back = pygame.image.load(r'images\image_back.png')
#creating middle
layer_middle = pygame.image.load(r'images\image_middle.png')
#creating front
layer_front = pygame.image.load(r'images\image_front.png')
#fundo
layer_fundo = pygame.image.load(r'images\fundo.png')

#creating list of layers
layers = [layer_fundo,layer_back,layer_middle,layer_front]
#####ARRUMAR O UPDATE PARA MOVER A TELA!!!!######
def update():
    for l in layers:
        global posx
        posx-= 5
        draw()
def draw():
    for l in layers:
        tela.blit(l , (posx,posy))
        pygame.display.flip()
        
    pygame.time.wait(500)
    update()

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

draw()
