import pygame, math
from config import *


class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = 70
        self.height = 100
        self.animation_loop = 0

        self.image = self.game.alucard_sprite_sheet.get_sprite(358, 4590, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        # self.collide()

    # def collide(self):
    #     hits = pygame.sprite.spritecollide(self, self.game.player2_group, False)
    #     if hits:
    #         self.game.player2_group.get_dmg(10)

    def animate(self):
        direction = self.game.player.direction

        animations = [
            self.game.alucard_sprite_sheet.get_sprite(359, 4594, self.width, self.height),
            self.game.alucard_sprite_sheet.get_sprite(197, 4699, self.width + 30, self.height + 50),
            self.game.alucard_sprite_sheet.get_sprite(362, 4705, self.width + 30, self.height + 45),
        ]

        if self.game.player.direction == "RIGHT":
            self.image = animations[math.floor(self.animation_loop)]
            self.image.set_colorkey(MAGENTA)
            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.flip(self.image, False, True)
            self.animation_loop += 0.15
            if self.animation_loop >= 3:
                self.kill()

        if self.game.player.direction == "LEFT":
            self.image = animations[math.floor(self.animation_loop)]
            self.image.set_colorkey(MAGENTA)
            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.flip(self.image, True, True)
            self.animation_loop += 0.15
            if self.animation_loop >= 3:
                self.kill()
