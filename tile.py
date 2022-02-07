import pygame
from setup import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        # inicia a classe pai
        super().__init__(groups)
        self.image = pygame.image.load('graphics/Test/Rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
