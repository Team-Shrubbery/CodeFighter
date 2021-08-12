import pygame
from config import *
from sprite_sheet import *

class Player2(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
      self.game = game
      self._layer = PLAYER_LAYER
      self.groups = self.game.all_sprites
      pygame.sprite.Sprite.__init__(self, self.groups)
      self.x = x
      self.y = y
      self.width = PLAYER_SIZE
      self.height = PLAYER_SIZE
      self.image = self.game.alucard_sprite_sheet.get_sprite(63, 771, self.width, self.height)
      self.image.set_colorkey(MAGENTA)
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y
      self.speed = 3


    def update(self):
      self.movement()


    def movement(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
        self.x -= self.speed
      if keys[pygame.K_d]:
        self.x += self.speed
      self.rect = (self.x, self.y, self.width, self.height)



