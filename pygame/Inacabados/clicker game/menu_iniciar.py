import pygame, sys, random
from escrita_por_letra import escrever_por_letra as escrever
from classes import Botao
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
botao_melhorar = pygame.image.load(r'imagens\b.png')
