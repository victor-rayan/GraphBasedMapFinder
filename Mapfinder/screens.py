from unicodedata import name
import pygame as pg
from button import *
import sys
from os import path
from const import *
import const as c

RES = c.WIDTH, c.HEIGHT
pygame.init()
game_surface = pygame.Surface(RES)
surface = pg.display.set_mode((c.WIDTH + 405, c.HEIGHT ))


bg_game = pg.image.load('backgroundgta.png').convert()

dir_icon = path.join(path.dirname(__file__), '../assets')

font = pygame.font.SysFont('Impact', 150)
text_font = pygame.font.SysFont('Impact', 80)

def get_font(size): 
    return pygame.font.Font(path.join(dir_icon, 'font.ttf'), size)
path.join(dir_icon, 'Play Rect.png')

def startgame():
    while True:
        
        surface.blit(game_surface, (0, 0))
        game_surface.blit(bg_game, (100, 60))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = ButtonScreen(image=pygame.image.load(path.join(dir_icon, 'Quit Rect.png')), pos=(WIDTH + 150, 200), 
                            text_input="START", font=get_font(20), base_color="White", hovering_color="Blue")
        JETTPACK = ButtonScreen(image=pygame.image.load(path.join(dir_icon, 'Quit Rect.png')), pos=(WIDTH + 150, 350), 
                            text_input="JETPACK", font=get_font(20), base_color="White", hovering_color="Blue")
        TERRESTRE = ButtonScreen(image=pygame.image.load(path.join(dir_icon, 'Quit Rect.png')), pos=(WIDTH + 150, 500), 
                            text_input="CARRO", font=get_font(20), base_color="White", hovering_color="Blue")                                         
        QUIT_BUTTON = ButtonScreen(image=pygame.image.load(path.join(dir_icon, 'Quit Rect.png')), pos=(WIDTH + 150, 650), 
                            text_input="SAIR", font=get_font(20), base_color="White", hovering_color="Blue")

        surface.blit(text_font.render('FindMap', True, pygame.Color('cyan'), True), (WIDTH + 10, 30))
        
        for button in [PLAY_BUTTON, JETTPACK, TERRESTRE, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(surface)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if():
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    startgame()     