import pygame

from configuracoes.constantes import ScreenWidth, White


class Placar:
    def __init__(self):
        self.Jogador1 = 0
        self.Jogador2 = 0
        self.Fonte = pygame.font.SysFont(None, 36)

    def Desenhar(self, tela):
        texto = self.Fonte.render(
            f"{self.Jogador1} - {self.Jogador2}",
            True,
            White,
        )

        tela.blit(
            texto,
            texto.get_rect(center=(ScreenWidth // 2, 30)),
        )