from config import *


class attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.x = y
        self.width = 100
        self.height = 145

        self.image = self.game.alucard_sprite_sheet.get_sprite(358, 5704, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.player2_group, True)

    def animate(self):
        direction = self.game.player.direction

        