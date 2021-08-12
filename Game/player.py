import pygame
import math
from config import *
from sprite_sheet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
      self.game = game
      self._layer = PLAYER_LAYER
      self.groups = self.game.all_sprites
      pygame.sprite.Sprite.__init__(self, self.groups)
      self.x = x
      self.y = y
      self.width = PLAYER_SIZE
      self.height = PLAYER_SIZE
      self.image = self.game.alucard_sprite_sheet.get_sprite(42, 185, self.width, self.height)
      self.image.set_colorkey(MAGENTA)
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y
      self.speed = 3
      self.facing = 'right'
      self.animation_loop = 1
      self.x_change = 0

    def update(self):
      self.movement()
      self.animate()
      self.rect.x += self.x_change
      self.collide_player('x')
      self.x_change = 0


    def movement(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
        self.x_change -= self.speed
        self.facing = 'left'
      if keys[pygame.K_RIGHT]:
        self.x_change += self.speed
        self.facing = 'right'
      self.rect = (self.x, self.y, self.width, self.height)

    def collide_player(self, direction):
      if direction == 'x':
        hits = pygame.sprite.collide_rect(player1, player2)
        if hits:
          if self.x_change > 0:
            self.rect.x = hits[0].rect.left - self.rect.width
          if self.x_change < 0:
            self.rect.x = hits[0].rect.right

    def animate(self):
      right_animations = [self.game.alucard_sprite_sheet.get_sprite(272, 771, self.width, self.height),
                          self.game.alucard_sprite_sheet.get_sprite(76, 770, self.width, self.height),
                          self.game.alucard_sprite_sheet.get_sprite(272, 771, self.width, self.height), 
                          self.game.alucard_sprite_sheet.get_sprite(59, 904, self.width, self.height)]
      
      if self.facing == 'right':
        if self.x_change == 0:
          self.image = self.game.alucard_sprite_sheet.get_sprite(42, 185, self.width, self.height)
          self.image.set_colorkey(MAGENTA)

        else:
          self.image = right_animations[math.floor(self.animation_loop)]
          self.image.set_colorkey(MAGENTA)
          self.animation_loop += 0.1
          if self.animation_loop > 4:
            self.animation_loop = 1





