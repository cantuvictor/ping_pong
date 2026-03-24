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


class Jogo:
    def __init__(self, tela):
        self.Tela  = tela
        self.Clock = pygame.time.Clock()

        self.Raquete1 = Raquete(15, ScreenHeight // 2 - 30)
        self.Raquete2 = Raquete(ScreenWidth - 25, ScreenHeight // 2 - 30)

        self.Bola   = Bola()
        self.Placar = Placar()
        self.Audio  = Audio()

    def ProcessarEntrada(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.Raquete1.MoverParaCima()
        if teclas[pygame.K_DOWN]:
            self.Raquete1.MoverParaBaixo()

    def Atualizar(self):
        self.Bola.Atualizar()
        colidiu = self.Bola.VerificarColisao(self.Raquete1, self.Raquete2)

        if colidiu:
            self.Audio.tocar_raquete()  # novo

        if self.Bola.X <= 0:
            self.Placar.Jogador2 += 1
            self.Audio.tocar_gol()      # novo
            self.Bola.Resetar()

        if self.Bola.X >= ScreenWidth:
            self.Placar.Jogador1 += 1
            self.Audio.tocar_gol()      # novo
            self.Bola.Resetar()

        if self.Raquete2.Rect.centery < self.Bola.Y:
            self.Raquete2.MoverParaBaixo()
        else:
            self.Raquete2.MoverParaCima()

    def Desenhar(self):
        self.Tela.fill(Black)
        self.Raquete1.Desenhar(self.Tela)
        self.Raquete2.Desenhar(self.Tela)
        self.Bola.Desenhar(self.Tela)
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