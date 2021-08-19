import pygame
from config import *
from sprite_sheet import *

class Ground(pygame.sprite.Sprite):
  def __init__(self, game, x, y):
    self.game = game
    self._layer = GROUND_LAYER
    self.groups = self.game.all_sprites
    pygame.sprite.Sprite.__init__(self, self.groups)
    self.x = x
    self.y = y
    self.width = 96
    self.height = 30
    self.image = self.game.ground_sprite_sheet.get_sprite(16, 28, self.width, self.height)
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    
