import pygame, math
from config import *

class Attack2(pygame.sprite.Sprite):
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
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.player_group, False)
        if hits:
            self.game.player -= self.game.player.current_health

    def animate(self):
        direction = self.game.player.direction

        animations = [self.game.alucard_sprite_sheet.get_sprite(67, 4694, self.width, self.height + 30),
                    self.game.alucard_sprite_sheet.get_sprite(208, 4700, self.width + 10, self.height + 50),
                    self.game.alucard_sprite_sheet.get_sprite(360, 4704, self.width + 30, self.height + 50),
                    self.game.alucard_sprite_sheet.get_sprite(71, 4864, self.width + 30, self.height + 35),
                    self.game.alucard_sprite_sheet.get_sprite(233, 4886, self.width + 45, self.height),
                    self.game.alucard_sprite_sheet.get_sprite(392, 4913, self.width + 40, self.height + 35)
                    ]

        if direction == "RIGHT":
            self.image = animations[math.floor(self.animation_loop)]
            self.image.set_colorkey(MAGENTA)
            self.image = pygame.transform.flip(self.image, False, True)
            self.animation_loop += 0.2
            if self.animation_loop >= 6:
                self.kill()

        if direction == "LEFT":
            self.image = animations[math.floor(self.animation_loop)]
            self.image.set_colorkey(MAGENTA)
            self.image = pygame.transform.flip(self.image, True, True)
            self.animation_loop += 0.2
            if self.animation_loop >= 6:
                self.kill()