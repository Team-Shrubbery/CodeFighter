import pygame, sys, random
from pygame.locals import *
from config import *
from data.player import *
from data.ground import *
from data.player2 import Player2

# ------------------------ Main Game Class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Code Fighter")
        # self.font = pygame.font.Font("resources/blackbone-font/Blackbone-0WxXR.ttf", 64)
        self.clock = pygame.time.Clock()
        self.playing = True

        # ----------------------- Sprite Sheets and image files to load ---------------------------
        self.background = pygame.image.load("resources/img/Battleback1.png")
        self.ground_image = pygame.image.load("resources/img/Ground.png")
        self.alucard_sprite_sheet = Spritesheet("resources/img/alucardfinal.png")

    # ----------------------- Putting sprites into groups and instantiatiating objects
    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.ground_group = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.player2 = pygame.sprite.LayeredUpdates()
        self.ground = Ground(self)
        self.player = Player(self)
        self.player2 = Player2(self)

    # -------------------------- handles different game events, can look up events in pygame docs ------------
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            # For events that occur upon clicking the mouse (left click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            # Event handling for a range of different key presses
            if event.type == pygame.KEYDOWN:
                pass

    # ------------------------ Update every sprite in the game/added to all_sprites group -------------------
    def update(self):
        self.all_sprites.update()

    # ------------------------ Draws on the screen ---------------------------
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    # -------------------------  Main game loop and update calls --------------
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.playing = False


# ------ starting the game --------
g = Game()
g.new()
while g.playing is True:
    g.main()

pygame.quit()
sys.exit()
