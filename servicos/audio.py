import os
import pygame

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SONS = os.path.join(BASE, "sons")


class Audio:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(8)

        self.som_raquete = self._carregar_som("raquete.mp3")
        self.som_raquete.set_volume(0.9)
        self.som_gol     = self._carregar_som("gol.mp3")

        fundo = os.path.join(SONS, "fundo.mp3")
        if os.path.exists(fundo):
            pygame.mixer.music.load(fundo)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1, 20.0)  # loop infinito

    def _carregar_som(self, nome):
        caminho = os.path.join(SONS, nome)
        if os.path.exists(caminho):
            som = pygame.mixer.Sound(caminho)
            som.set_volume(0.7)
            return som
        return None

    def tocar_raquete(self):
        if self.som_raquete:
            self.som_raquete.play()

    def tocar_gol(self):
        if self.som_gol:
            self.som_gol.play()