import pygame
import sys
from config import *
from game_over import *
from intro import *
from player import *
from sprite_sheet import *
from player2 import *

class Game:
    def __init__(self):
        # pygame.__init__()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.alucard_sprite_sheet = Spritesheet('../img/alucardfinal.png')
        self.background = pygame.image.load('../img/battleback1.png')

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 1, 260)
        self.player2 = Player2(self, 600, 260)
        
    def events(self):
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.playing = False
            self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
          self.events()
          self.update()
          self.draw()
        self.running = False

g = Game()
g.new()
while g.running is True:
  g.main()


pygame.quit()
sys.exit()