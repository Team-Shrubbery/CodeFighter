import pygame, sys, random
from pygame.locals import *
from pygame.sprite import Sprite
from config import *
from data.player import *
from data.player2 import *
from data.ground import *
from data.button import *
# from healthbar import *

# ------------------------ Main Game Class
class Game:
      def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
            pygame.display.set_caption("Code Fighter")
            self.font = pygame.font.Font("resources/fonts/arial.ttf", 128)
            self.clock = pygame.time.Clock()
            self.playing = True

# ----------------------- Sprite Sheets and image files to load ---------------------------
            self.background = pygame.image.load('resources/img/Battleback1.png')
            self.ground_image = pygame.image.load('resources/img/Ground.png')
            self.alucard_sprite_sheet = Spritesheet('resources/img/alucardfinal.png')
            self.intro_background = pygame.image.load('resources/img/wizardtower.png')
            self.fixer_sprite_sheet = Spritesheet('resources/img/thefixer.png')

      def intro_screen(self):
            intro = True

            title = self.font.render('Code Fighter', True, BLUE)
            title_rect = title.get_rect(x=10,y=10)
            play_button = Button(WIN_WIDTH // 2,WIN_HEIGHT // 2,100,50, RED, BLACK, 'Play', 32)


            while intro:
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              intro = False
                              self.running = False

                        mouse_pos = pygame.mouse.get_pos()
                        mouse_pressed = pygame.mouse.get_pressed()

                        if play_button.is_pressed(mouse_pos, mouse_pressed):
                              intro = False

                        self.intro_background = pygame.transform.scale(self.intro_background, (WIN_WIDTH, WIN_HEIGHT))
                        self.screen.fill(GREY)
                        self.screen.blit(title, title_rect)
                        self.screen.blit(play_button.image, play_button.rect)

                        self.clock.tick(FPS)
                        pygame.display.update()

# ----------------------- Putting sprites into groups and instantiatiating objects
      def new(self):
            self.all_sprites = pygame.sprite.LayeredUpdates()
            self.ground_group = pygame.sprite.LayeredUpdates()
            # self.health_bar = pygame.sprite.LayeredUpdates()
            self.player1_group = pygame.sprite.LayeredUpdates()
            self.player2_group = pygame.sprite.LayeredUpdates()
            # self.healthbar = Healthbar(self)
            self.ground = Ground(self)
            self.player = Player(self)
            self.player2 = Player2(self)

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

# -------------------------- handles different game events, can look up events in pygame docs ------------
      def events(self):
            for event in pygame.event.get():
                  if event.type == QUIT:
                        self.playing = False
                  # For events that occur upon clicking the mouse (left click) 
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        pass
            
                  # Event handling for a range of different key presses    
                  if event.type == pygame.KEYDOWN:
                        if self.player:
                              if event.key == pygame.K_SPACE:
                                    self.player.jump()
                              if event.key == pygame.K_f:
                                    self.player.attack()

                        if self.player2:
                              if event.key == pygame.K_w:
                                    self.player2.jump()
                              if event.key == pygame.K_d:
                                    self.player2.attacking = True
                                    self.player2.attack()

                  # if event.type == pygame.KEYUP:
                  #       if self.player2:
                  #             if event.key == K_d:
                  #                   self.player2.attacking = False

      
      # def basic_health(self):
      #       pygame.draw.line(self.screen, GREEN, (0,30),(0, 30) , self.player.current_health)
      #             if self.player.current_health < self.player.max_health / 2:
      #                   pygame.draw.line(self.screen, YELLOW, (0,30),(0, 30) , self.player.current_health)

      #             if self.player.current_health < self.player.max_health / 4:
      #                   pygame.draw.line(self.screen, RED, (0,30),(0, 30) , self.player.current_health)


# ------ starting the game --------
g = Game()
g.intro_screen()
g.new()
while g.playing is True:
      g.main()

pygame.quit()
sys.exit()