import pygame
from configuracoes.constantes import ScreenHeight, White

class Raquete:
    def __init__(self, x, y, largura=10, altura=60, velocidade=5):
        self.Rect = pygame.Rect(x, y, largura, altura)
        self.Velocidade = velocidade

    def MoverParaCima(self):
        if self.Rect.top > 0:
            self.Rect.y -= self.Velocidade

    def MoverParaBaixo(self):
        if self.Rect.bottom < ScreenHeight:
            self.Rect.y += self.Velocidade

    def Desenhar(self, tela):
        pygame.draw.rect(tela, White, self.Rect)