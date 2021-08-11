import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
      self.game = game
      self.player = PLAYER_LAYER
      self.groups = self.game.all_sprites
      pygame.sprite.Sprite.__init__(self, self.groups)
      self.x = x
      self.y = y
      self.width = 32
      self.height = 32
      self.image = pygame.Surface((self.width, self.height))
      self.image.fill(RED)
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y

    def update(self):
      pass

