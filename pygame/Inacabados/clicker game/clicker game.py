import pygame, sys, random
from escrita_por_letra import escrever_por_letra as escrever
from classes import Botao, Personagem, Item, Monstro, chao
from vars import sair_do_jogo
import vars as v


##inicializando pygame##

#pygame#
relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption('GameClickerDev')
tela = pygame.display.set_mode((v.largura,v.altura))
tela.fill((0,0,0))

#fontes#
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)

#botoes#
botao_iniciar = pygame.image.load(r'imagens\iniciar.png')
botao_iniciar_press = pygame.image.load(r'imagens\iniciar_press.png')
botao_sair = pygame.image.load(r'imagens\sair.png')
botao_sair_press = pygame.image.load(r'imagens\sair_press.png')
botao_aleatorio = pygame.image.load(r'imagens\aleatorio.png')
botao_aleatorio_press = pygame.image.load(r'imagens\aleatorio_press.png')
botao_melhorar = pygame.image.load(r'imagens\melhorar.png')
botao_melhorar_press = pygame.image.load(r'imagens\melhorar_press.png')


##fim da inicialização do pygame##

#####INICIO DO CODIGO DO JOGO#####
nome = fonte.render("Escolha seu nome: ", 1, (255,255,255))
tela.blit(nome, (25,25))
pygame.display.update()

###DEFINIR NOME POR INPUT###
while v.game_on == True:
   
   for event in pygame.event.get():
      sair_do_jogo()
      #receber nome#
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RETURN:
            v.display_class = True
            tela.fill((0,0,0))
            v.game_on = False
         if event.key == pygame.K_BACKSPACE:
            v.input_usuario = v.input_usuario[:-1]
            tela.fill((0,0,0))
            tela.blit(nome, (25,25))
            pygame.display.flip()
         else:
            v.input_usuario += event.unicode
            
   #mostrar nome na tela#          
   mostrar_texto = fonte.render(v.input_usuario, 1, (255,255,255))
   lim_sizex, lim_sizey = 800,800
   mostrar_texto_limpar = pygame.Rect(25,60,lim_sizex,lim_sizey)
   pygame.draw.rect(tela,(0,0,0),mostrar_texto_limpar)
   tela.blit(mostrar_texto,(25,60))
   pygame.display.update()
###FIM DA DEFINIÇÃO POR INPUT###
   
###LIMPANDO A TELA E FAZENDO AJUSTES###
tela.fill((0,0,0))
pygame.display.update()
frase = 'Game Start!!   '
escrever(frase,300,260,(255,255,255),tela,200)
tela.fill((0,0,0))
pygame.display.update()
v.input_usuario = v.input_usuario[:-1]

###DEFININDO AS CLASSES###
item_arma = Item()
char = Personagem(item_arma)
chao = chao()
char.mostrar_level()
char.mostrar_dano()
char.name(v.input_usuario)
monstro = Monstro(v.game_level)
botao_melhorar = Botao(v.botao_posx,0,1.5,botao_melhorar,botao_melhorar_press)
botao_aleatorio = Botao(v.botao_posx,50,1.5,botao_aleatorio,botao_aleatorio_press)



###INICIO DO JOGO###
while v.display_class == True:
    #CRIAR MOB#
    if v.novo_mob:
        sair_do_jogo()
        monstro = Monstro(v.game_level)
        v.novo_mob = False
    else:
        #blitar tela do jogo#
        sair_do_jogo()
        monstro.limpar_monstro()
        monstro.desenhar_monstro()        
        char.limpar_char()
        char.desenhar_char()
        item_arma.limpar_item()
        item_arma.desenhar_item(tela)        
        chao.desenhar()
        monstro.vida()
        botao_melhorar.desenhar(tela)
        botao_aleatorio.desenhar(tela)
        #detectar clique do mouse#
        for event in pygame.event.get():
            sair_do_jogo()
            if pygame.mouse.get_pressed() == (1,0,0):
                #definir retas para usar collidepoint#
                posicao_mouse = pygame.mouse.get_pos()
                mob_reta = monstro.reta_monstro
                melhorar_reta = botao_melhorar.rect
                aleatorio_reta = botao_aleatorio.rect
                
                #collidepoint para o monstro#
                if pygame.Rect.collidepoint(mob_reta,posicao_mouse):
                    monstro.clicou(char)
                    char.limpar_level()
                    char.mostrar_level()
                    char.limpar_dano()
                    char.mostrar_dano()
                    pygame.display.flip()
                if pygame.Rect.collidepoint(melhorar_reta,posicao_mouse):
                    botao_melhorar.desenhar_clique(tela)
                    item_arma.melhorar_item(char)
                    item_arma.limpar_item()
                    item_arma.desenhar_item(tela)                    
                    char.limpar_dano()
                    char.mostrar_dano()
                    pygame.display.flip()
                    pygame.time.delay(200)
                    
                if pygame.Rect.collidepoint(aleatorio_reta,posicao_mouse):
                    botao_aleatorio.desenhar_clique(tela)
                    item_arma.item_aleatorio(char,tela)
                    item_arma.limpar_item()
                    item_arma.desenhar_item(tela)                    
                    char.limpar_dano()
                    char.mostrar_dano()
                    pygame.display.flip()
                    pygame.time.delay(200)
                    
        pygame.display.flip()
