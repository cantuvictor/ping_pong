import sys

import pygame

from interface.menu_principal import MenuPrincipal
from servicos.jogo import Jogo
from configuracoes.constantes import (
    ScreenHeight,
    ScreenWidth,
)


def Main():
    pygame.init()

    tela = pygame.display.set_mode(
        (ScreenWidth, ScreenHeight)
    )

    pygame.display.set_caption("Pong")

    menu = MenuPrincipal(tela)

    while True:
        menu.Exibir()

        jogo = Jogo(tela)
        if not jogo.Executar():
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    Main()