
from background import WHITE, SIZE_WINDOW_Y, SIZE_WINDOW_X, draw_stars
import pygame


# pygame.quit() => termina a execução

class GameOver(pygame.sprite.Sprite):

    def __init__(self, display, font, color, info):
       
       #configurações iniciais
        self.display = display
        self.display.fill(color)
        fonte_texto = pygame.font.Font(font, 40)
        fonte_buttom = pygame.font.Font(font, 10)
        draw_stars(self.display)

        # setando mensagem (posição)
        texto = fonte_texto.render(info, True, (255, 255, 255))
        pos_texto = texto.get_rect(center=(SIZE_WINDOW_X//2, 50))
        self.display.blit(texto, pos_texto)

       # cria superfície do botão e seta size
        self.button_surface = pygame.Surface((150, 50))
        self.button_rect = pygame.Rect((SIZE_WINDOW_X//2) - 200, (SIZE_WINDOW_Y//2) - 50, 150, 50)

        self.button_surface_out = pygame.Surface((150, 50))
        self.button_rect_out = pygame.Rect((SIZE_WINDOW_X//2) + 50, (SIZE_WINDOW_Y//2) - 50, 150, 50)

        # cria o retângulo do botão e seta cor
        pygame.draw.rect(self.button_surface, (255,255,255), (0, 0, 0, 0), 2)
        pygame.draw.rect(self.button_surface_out, (255,255,255), (0, 0, 0, 0))

        #integra retangulo com a superfície
        self.display.blit(self.button_surface, self.button_rect)
        self.display.blit(self.button_surface_out, self.button_rect_out)

        self.display.blit(fonte_buttom.render('Reiniciar!', True, (255,255,255)), (self.button_rect.centerx - 50, self.button_rect.centery))
        self.display.blit(fonte_buttom.render('Sair!', True, (255,255,255)), (self.button_rect_out.centerx - 50, self.button_rect_out.centery))
        #self.button_rect.blit(texto_botao, pos_texto_botao)

    def getReturnButton(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    return False
                if self.button_rect_out.collidepoint(event.pos):
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
        return True