from config import *

class Healthbar(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        # self.image = pygame.draw.line(self.game.screen, GREEN, (0,30),(0, 30) , MAX_HEALTH)
        # self.rect = self.image.get_rect()
        # self.groups = self.game.all_sprites, self.game.health_bar
        pygame.sprite.Sprite.__init__(self, self.groups)
    
    def basic_health(self):
        pygame.draw.line(self.game.screen, GREEN, (0,30),(0, 30) , self.game.player.current_health)
        if self.game.player.current_health < self.game.player.max_health / 2:
            pygame.draw.line(self.game.screen, YELLOW, (0,30),(0, 30) , self.game.player.current_health)

        if self.game.player.current_health < self.game.player.max_health / 4:
            pygame.draw.line(self.game.screen, RED, (0,30),(0, 30) , self.game.player.current_health)

    def update(self):
        self.basic_health()