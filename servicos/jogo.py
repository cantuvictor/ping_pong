import random

import pygame

from dominio.bola import Bola
from dominio.placar import Placar
from dominio.raquete import Raquete
from servicos.audio import Audio
from configuracoes.constantes import (
    Black,
    ScreenHeight,
    ScreenWidth,
)

CORES_DISTRATORAS = [
    (255, 80,  80),
    (80,  255, 80),
    (80,  80,  255),
    (255, 255, 80),
    (255, 80,  255),
    (80,  255, 255),
    (255, 165, 0),
]


class BolaDistratora:
    """Bola visual apenas — rebate nas bordas, some ao sair pelos lados."""
    def __init__(self, x, y, vx, vy, cor):
        self.X  = x
        self.Y  = y
        self.VX = vx
        self.VY = vy
        self.Cor = cor
        self.Tamanho = 7
        self.Ativa = True

    def Atualizar(self):
        self.X += self.VX
        self.Y += self.VY

        # rebate nas bordas superior e inferior
        if self.Y <= 0:
            self.Y = 1
            self.VY = abs(self.VY)
        elif self.Y >= ScreenHeight:
            self.Y = ScreenHeight - 1
            self.VY = -abs(self.VY)

        # some apenas pelos lados (gol)
        if self.X < 0 or self.X > ScreenWidth:
            self.Ativa = False

    def Desenhar(self, tela):
        if self.Ativa:
            pygame.draw.circle(tela, self.Cor, (int(self.X), int(self.Y)), self.Tamanho)


class Jogo:
    def __init__(self, tela):
        self.Tela  = tela
        self.Clock = pygame.time.Clock()

        self.Raquete1 = Raquete(15, ScreenHeight // 2 - 30)
        self.Raquete2 = Raquete(ScreenWidth - 25, ScreenHeight // 2 - 30)

        self.BolaPrincipal    = Bola()
        self.BolasDistratoras = []
        self.Placar = Placar()
        self.Audio  = Audio()

        self._ultimo_fragmento_ms = pygame.time.get_ticks()

    def _fragmentar(self):
        """Gera 3 bolas distratoras na posicao atual indo na mesma direcao da bola."""
        cores = random.sample(CORES_DISTRATORAS, 3)
        for cor in cores:
            vx = abs(self.BolaPrincipal.VelocidadeX)  # sempre positivo
            if self.BolaPrincipal.VelocidadeX < 0:    # aplica o sinal correto
                vx *= -1
            vy = random.uniform(-4, 4)
            nova = BolaDistratora(
                self.BolaPrincipal.X,
                self.BolaPrincipal.Y,
                vx, vy, cor
            )
            self.BolasDistratoras.append(nova)
        self._ultimo_fragmento_ms = pygame.time.get_ticks()

    def ProcessarEntrada(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.Raquete1.MoverParaCima()
        if teclas[pygame.K_DOWN]:
            self.Raquete1.MoverParaBaixo()

    def Atualizar(self):
        # -- Bola principal --
        self.BolaPrincipal.Atualizar()
        colidiu = self.BolaPrincipal.VerificarColisao(self.Raquete1, self.Raquete2)

        if colidiu:
            self.Audio.tocar_raquete()

            # fragmenta apenas se ja passaram 5s desde o ultimo fragmento
            agora = pygame.time.get_ticks()
            if agora - self._ultimo_fragmento_ms >= 5000:
                self._fragmentar()

        # -- Bolas distratoras: so movem, sem fisica --
        for b in self.BolasDistratoras:
            b.Atualizar()
        self.BolasDistratoras = [b for b in self.BolasDistratoras if b.Ativa]

        # -- Gol (apenas bola principal) --
        if self.BolaPrincipal.X < 0:
            self.Placar.Jogador2 += 1
            self.Audio.tocar_gol()
            self.BolaPrincipal.Resetar()
            self.BolasDistratoras.clear()
            self._ultimo_fragmento_ms = pygame.time.get_ticks()

        elif self.BolaPrincipal.X > ScreenWidth:
            self.Placar.Jogador1 += 1
            self.Audio.tocar_gol()
            self.BolaPrincipal.Resetar()
            self.BolasDistratoras.clear()
            self._ultimo_fragmento_ms = pygame.time.get_ticks()

        # -- IA segue a bola principal --
        if self.Raquete2.Rect.centery < self.BolaPrincipal.Y - 5:
            self.Raquete2.MoverParaBaixo()
        elif self.Raquete2.Rect.centery > self.BolaPrincipal.Y + 5:
            self.Raquete2.MoverParaCima()

    def Desenhar(self):
        self.Tela.fill(Black)

        self.Raquete1.Desenhar(self.Tela)
        self.Raquete2.Desenhar(self.Tela)

        for b in self.BolasDistratoras:
            b.Desenhar(self.Tela)

        self.BolaPrincipal.Desenhar(self.Tela)
        self.Placar.Desenhar(self.Tela)

        pygame.display.flip()

    def Executar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
            self.ProcessarEntrada()
            self.Atualizar()
            self.Desenhar()
            self.Clock.tick(60)