import pygame
from config import *

class Ground(pygame.sprite.Sprite):
      def __init__(self, game):
            self.game = game
            self.groups = self.game.all_sprites, self.game.ground_group
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.image = pygame.image.load("resources/img/Ground.png")
            self.rect = self.image.get_rect(center = (350, 600))
      

