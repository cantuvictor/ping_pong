import random

import pygame

from configuracoes.constantes import (
    ScreenHeight,
    ScreenWidth,
    White,
)


class Bola:
    def __init__(self, tamanho=7):
        self.Tamanho = tamanho
        self.Resetar()

    def Resetar(self):
        self.X = ScreenWidth // 2
        self.Y = ScreenHeight // 2

        self.VelocidadeX = random.choice([-5, 5])
        self.VelocidadeY = random.choice(
            [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        )

    def Atualizar(self):
        self.X += self.VelocidadeX
        self.Y += self.VelocidadeY

        if self.Y <= 0 or self.Y >= ScreenHeight:
            self.VelocidadeY *= -1

    def VerificarColisao(self, raquete1, raquete2):
        rect = pygame.Rect(
            self.X,
            self.Y,
            self.Tamanho,
            self.Tamanho,
        )

        if rect.colliderect(raquete1.Rect) or \
           rect.colliderect(raquete2.Rect):
            self.VelocidadeX *= -1

    def Desenhar(self, tela):
        pygame.draw.circle(tela, White, (self.X, self.Y), self.Tamanho)