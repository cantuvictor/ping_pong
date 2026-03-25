import random
import math

import pygame

from configuracoes.constantes import (
    ScreenHeight,
    ScreenWidth,
    White,
)

VELOCIDADE = 5


class Bola:
    def __init__(self, tamanho=7, cor=None):
        self.Tamanho = tamanho
        self.Cor = cor or White
        self.Resetar()

    def Resetar(self):
        self.X = ScreenWidth // 2
        self.Y = ScreenHeight // 2

        self.VelocidadeX = random.choice([-VELOCIDADE, VELOCIDADE])
        self.VelocidadeY = random.choice([-3, -2, 2, 3])

    def _novo_angulo(self, inverteu_y=False):
        variacao = math.radians(random.uniform(-20, 20))
        angulo = math.atan2(self.VelocidadeY, self.VelocidadeX) + variacao

        sinal_x = 1 if self.VelocidadeX >= 0 else -1
        angulo_ref = 0 if sinal_x > 0 else math.pi
        limite = math.radians(50)

        diff = (angulo - angulo_ref + math.pi) % (2 * math.pi) - math.pi
        if abs(diff) > limite:
            angulo = angulo_ref + math.copysign(limite, diff)

        self.VelocidadeX = VELOCIDADE * math.cos(angulo)
        self.VelocidadeY = VELOCIDADE * math.sin(angulo)

        if inverteu_y:
            if self.Y <= 0 and self.VelocidadeY < 0:
                self.VelocidadeY *= -1
            elif self.Y >= ScreenHeight and self.VelocidadeY > 0:
                self.VelocidadeY *= -1

        if abs(self.VelocidadeY) < 1.5:
            self.VelocidadeY = math.copysign(1.5, self.VelocidadeY)
            if inverteu_y:
                if self.Y <= 0:
                    self.VelocidadeY = 1.5
                elif self.Y >= ScreenHeight:
                    self.VelocidadeY = -1.5

    def Atualizar(self):
        self.X += self.VelocidadeX
        self.Y += self.VelocidadeY

        if self.Y <= 0:
            self.Y = 2
            self.VelocidadeY = abs(self.VelocidadeY)
            self._novo_angulo(inverteu_y=True)

        elif self.Y >= ScreenHeight:
            self.Y = ScreenHeight - 2
            self.VelocidadeY = -abs(self.VelocidadeY)
            self._novo_angulo(inverteu_y=True)

    def VerificarColisao(self, raquete1, raquete2):
        rect = pygame.Rect(self.X, self.Y, self.Tamanho, self.Tamanho)
        colidiu = rect.colliderect(raquete1.Rect) or rect.colliderect(raquete2.Rect)

        if colidiu:
            self.VelocidadeX *= -1
            self._novo_angulo()

        return colidiu

    def Desenhar(self, tela):
        pygame.draw.circle(tela, self.Cor, (int(self.X), int(self.Y)), self.Tamanho)