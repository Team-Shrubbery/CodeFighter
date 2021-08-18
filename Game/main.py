from data.attack2 import Attack2
import pygame, sys, random
from pygame.locals import *
from config import *
from data.player import *
from data.ground import *
from data.player2 import Player2
from data.button import *
from sockets1 import SocketConnection


# ------------------------ Main Game Class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Code Fighter")
        self.font = pygame.font.Font("resources/fonts/arial.ttf", 128)
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("resources/img/battleback1.png")
        self.ground_image = pygame.image.load("resources/img/Ground.png")
        self.alucard_sprite_sheet = Spritesheet("resources/img/alucardfinal.png")
        self.fixer_sprite_sheet = Spritesheet("resources/img/thefixer.png")

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.ground_group = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.attacks2 = pygame.sprite.LayeredUpdates()
        self.player_group = pygame.sprite.LayeredUpdates()
        self.player2_group = pygame.sprite.LayeredUpdates()
        self.ground = Ground(self)
        self.player = Player(self)
        self.player2 = Player2(self)

        self.playing = True
        self.round_counter = 1
        self.fighting = False
        self.player_wins = 0
        self.player2_wins = 0

    def intro_screen(self):

        intro = True
        intro_background = pygame.image.load("resources/img/battleback3.png")
        title_font = pygame.font.SysFont(None, 160)
        title = title_font.render("Code Fighter", True, RED)
        play_button = Button((WIN_WIDTH // 2 - 200), (WIN_HEIGHT // 2) + 100, 100, 50, RED, BLACK, "Play", 32)
        quit_button = Button((WIN_WIDTH // 2 + 100), (WIN_HEIGHT // 2) + 100, 100, 50, RED, BLACK, "Exit", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.playing = False

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if play_button.is_pressed(mouse_pos, mouse_pressed):
                    intro = False

                if quit_button.is_pressed(mouse_pos, mouse_pressed):
                    intro = False
                    self.playing = False

                self.screen.fill(GREY)
                self.screen.blit(intro_background, (0, 0))
                self.screen.blit(title, (55, 225))  # DONE
                self.screen.blit(play_button.image, play_button.rect)
                self.screen.blit(quit_button.image, quit_button.rect)

                self.clock.tick(FPS)
                pygame.display.update()

    # ----------------------- Putting sprites into groups and instantiatiating objects
    def new(self):
        # # self.sockets = SocketConnection()
        # self.sockets.start_connection()
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.ground_group = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.attacks2 = pygame.sprite.LayeredUpdates()
        self.player_group = pygame.sprite.LayeredUpdates()
        self.player2_group = pygame.sprite.LayeredUpdates()
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

        if self.player.attacking == True:
            if self.player.direction == "RIGHT":
                Attack(self, self.player.rect.x + 70, self.player.rect.y - 20)
            if self.player.direction == "LEFT":
                Attack(self, self.player.rect.x - 70, self.player.rect.y - 20)

        if self.player2.attacking == True:
            if self.player2.direction == "RIGHT":
                Attack2(self, self.player2.rect.x + 70, self.player2.rect.y - 20)
            if self.player2.direction == "LEFT":
                Attack2(self, self.player2.rect.x - 70, self.player2.rect.y - 20)

    # ------------------------ Update every sprite in the game/added to all_sprites group -------------------
    def update(self):
        self.all_sprites.update()

    # ------------------------ Draws on the screen ---------------------------
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.display_round()
        self.player.basic_health()
        self.player.character_name()
        self.player2.basic_health()
        self.player2.character_name()
        self.win_display()
        self.game_over()
        self.clock.tick(FPS)
        pygame.display.update()

    def display_round(self):
        font = pygame.font.SysFont(None, 30)
        img = font.render("ROUND", True, BLACK)
        self.screen.blit(img, (365, 10))
        pygame.draw.circle(self.screen, RED, (400, 60), 30, 0)
        font2 = pygame.font.SysFont(None, 35)
        img2 = font2.render(f"{self.round_counter}", True, WHITE)
        self.screen.blit(img2, (392, 47))

    # -------------------------  Main game loop and update calls --------------
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.playing = False

    def win_display(self):
        # if self.player.dead == True:
        #     self.player2_wins += 1
        # if self.player2.dead == True:
        #     self.player_wins += 1

        self.font = pygame.font.Font("resources/fonts/arial.ttf", 28)
        textstr = str(f"{self.player_wins} WINS")
        text = self.font.render(textstr, True, BLACK)
        text_rect = text.get_rect(x=10, y=80)
        self.screen.blit(text, text_rect)

        textstr = str(f"{self.player2_wins} WINS")
        text = self.font.render(textstr, True, BLACK)
        text_rect = text.get_rect(x=(WIN_WIDTH // 2) + 290, y=80)
        self.screen.blit(text, text_rect)

    def game_over(self):
        play_button = Button(WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2, 100, 50, RED, BLACK, "Play Again", 16)
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        self.font = pygame.font.Font("resources/fonts/arial.ttf", 64)

        if self.player.dead or self.player2.dead == True:
            self.screen.blit(play_button.image, play_button.rect)

        if self.player2.dead == True:
            text = self.font.render("PLAYER ONE WINS", True, BLUE)
            text_rect = text.get_rect(x=20, y=100)
            self.screen.blit(text, text_rect)

        if self.player.dead == True:
            text = self.font.render("PLAYER TWO WINS", True, BLUE)
            text_rect = text.get_rect(x=20, y=100)
            self.screen.blit(text, text_rect)

        if play_button.is_pressed(mouse_pos, mouse_pressed):
            g.new()


# ------ starting the game --------

g = Game()
g.intro_screen()
g.new()


while g.playing is True:
    g.main()
    # g.game_over()

pygame.quit()
sys.exit()
