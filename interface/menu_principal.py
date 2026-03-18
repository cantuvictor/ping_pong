import pygame
import sys

from configuracoes.constantes import (
    Black,
    ScreenHeight,
    ScreenWidth,
    White,
)


class MenuPrincipal:
    def __init__(self, tela):
        self.Tela = tela
        self.FonteTitulo = pygame.font.SysFont(None, 50)
        self.FonteBlink = pygame.font.SysFont(None, 26)

    def Exibir(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return True

            self.Tela.fill(Black)

            titulo = self.FonteTitulo.render(
                "Pong",
                True,
                White,
            )

            self.Tela.blit(
                titulo,
                titulo.get_rect(
                    center=(ScreenWidth // 2, ScreenHeight // 2)
                ),
            )

            if pygame.time.get_ticks() % 2000 < 1000:
                texto = self.FonteBlink.render(
                    "Pressione ESPAÇO",
                    True,
                    White,
                )

                self.Tela.blit(
                    texto,
                    texto.get_rect(
                        center=(
                            ScreenWidth // 2,
                            ScreenHeight // 2 + 50,
                        )
                    ),
                )

            pygame.display.flip()