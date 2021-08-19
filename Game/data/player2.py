import pygame, math
from pygame.locals import *
from data.sprite_sheet import *
from data.attack2 import *
from config import *


# -------------- Player Class ------------------
class Player2(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        self.opponent_character = self.game.sockets.get_player2_character()
        if self.opponent_character == "Alucard":
            print("this got triggered line 15 player2")
            self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
            self.image.set_colorkey(MAGENTA)
        else:
            print("this got triggered line 19 player2")
            self.image = self.game.fixer_sprite_sheet.get_sprite(130, 5, 100, 120)
            self.image.set_colorkey(MAGENTA2)

        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites, self.game.player2_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 100
        self.height = 120

        # ------------- Health & Health Bar ----------------

        self.cur_health = CUR_HEALTH
        self.max_health = MAX_HEALTH
        self.healthbar_length = 300  # pixels
        self.health_ratio = self.max_health / self.healthbar_length
        self.dead = False
        self.death_frame = 0

        # --------------- Position and Direction -------------
        self.vx = 0
<<<<<<< HEAD
        # self.pos = vec((640, 240))
        self.pos = vec((self.game.sockets.get_player2_x(), 240))
=======
        self.pos = vec((640, 240))
        # self.pos = vec((self.game.sockets.get_player1_x(), 240))
>>>>>>> dec7264b5c8341e837e82c0a98899cec95dea517
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # -------------- Movement --------------
<<<<<<< HEAD
        self.direction = self.game.sockets.get_player2_direction()
=======
        self.direction = "LEFT"
>>>>>>> dec7264b5c8341e837e82c0a98899cec95dea517
        self.jumping = False
        self.running = False
        self.move_frame = 0

        # ----------- Combat ---------------------
        self.attacking = False
        # self.cooldown = False
        self.attack_frame = 0

    def move(self):
        self.acc = vec(0, 0.5)
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # # --------- keyboard input ----------------
        opponent_move = self.game.sockets.get_opponent_move()
        if opponent_move == "left":
            self.acc.x = -ACC
            self.direction = "LEFT"
            self.game.sockets.reset_opponent_move()
        if opponent_move == "right":
            self.acc.x = ACC
            self.direction = "RIGHT"
            self.game.sockets.reset_opponent_move()

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        self.rect.midbottom = self.pos

    def attack_keys(self):
        opponent_move = self.game.sockets.get_opponent_move()
        if opponent_move == "attack":
            self.attacking = True
            self.attack_animation()
            self.game.sockets.reset_opponent_move()

        if opponent_move == "jump":
            self.jump()
<<<<<<< HEAD
            self.game.sockets.reset_opponent_move()
=======
>>>>>>> dec7264b5c8341e837e82c0a98899cec95dea517

    def player_in_place(self):
        if self.running == False and self.attacking == False:
            if self.direction == "RIGHT":
                self.image = self.game.fixer_sprite_sheet.get_sprite(124, 5, 130, 125)
                self.image.set_colorkey(MAGENTA2)
            if self.direction == "LEFT":
                self.image = self.game.fixer_sprite_sheet.get_sprite(124, 5, 130, 125)
                self.image.set_colorkey(MAGENTA2)
                self.image = pygame.transform.flip(self.image, True, False)

    def gravity_check(self):
        # hits = collide with anything in the ground_group
        hits = pygame.sprite.spritecollide(self, self.game.ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    # ---------- method calls -----------
    def update(self):
        self.player_in_place()
        self.move()
        self.gravity_check()
        self.animate_move()
        self.collide_player()
        self.attack_keys()
        self.attack_animation()
        self.collide_attack()
        self.animate_death()

    def animate_move(self):
        self.run_ani = [
            self.game.fixer_sprite_sheet.get_sprite(536, 137, 85, 124),
            self.game.fixer_sprite_sheet.get_sprite(513, 261, 97, 125),
            self.game.fixer_sprite_sheet.get_sprite(448, 134, 89, 124),
        ]

        if self.move_frame > 3:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                if self.direction == "RIGHT":
                    self.image = self.run_ani[math.floor(self.move_frame)]
                    self.image.set_colorkey(MAGENTA2)
            elif self.vel.x < 0:
                if self.direction == "LEFT":
                    self.image = self.run_ani[math.floor(self.move_frame)]
                    self.image.set_colorkey(MAGENTA2)
                    self.image = pygame.transform.flip(self.image, True, False)

            self.move_frame += 0.1

        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = self.run_ani[self.move_frame]
            elif self.direction == "LEFT":
                self.image = self.run_ani[self.move_frame]

    # ----- correction for pygame attack error when attacking left ----------
    def correction(self):
        if self.attack_frame == 1:
            self.pos.x -= 20
        if self.attack_frame == 4:
            self.pos.x += 20

    def attack_animation(self):
        attack_ani = [
            self.game.fixer_sprite_sheet.get_sprite(465, 416, self.width + 20, self.height - 10),
            self.game.fixer_sprite_sheet.get_sprite(0, 0, self.width + 20, self.height - 10),
            self.game.fixer_sprite_sheet.get_sprite(180, 562, self.width + 50, self.height - 10),
            self.game.fixer_sprite_sheet.get_sprite(340, 566, self.width + 20, self.height - 15),
            self.game.fixer_sprite_sheet.get_sprite(256, 11, self.width + 30, self.height - 20),
        ]

        if self.attacking == True:
            if self.direction == "RIGHT":
                self.image = attack_ani[math.floor(self.attack_frame)]
                self.image.set_colorkey(MAGENTA2)
                self.attack_frame += 0.1
                if self.attack_frame >= 5:
                    self.attack_frame = 1
                    self.attacking = False

            if self.direction == "LEFT":
                self.image = attack_ani[math.floor(self.attack_frame)]
                self.image.set_colorkey(MAGENTA2)
                self.image = pygame.transform.flip(self.image, True, False)
                self.attack_frame += 0.1
                if self.attack_frame >= 5:
                    self.attack_frame = 1
                    self.attacking = False

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.ground_group, False)

        self.rect.x -= 1

        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

    # -------- HEALTH & DAMAGE --------

    def get_damage(self, amount):  # subtracts health
        if self.cur_health > 0:
            self.cur_health -= amount
        if self.cur_health <= 0:
            self.cur_health = 0

    def get_health(self, amount):  # adds health
        if self.cur_health > self.max_health:
            self.cur_health += amount
        if self.cur_health >= self.max_health:
            self.cur_health = self.max_health

    def basic_health(self):  # draws the health bar inside a box
        if self.cur_health <= (MAX_HEALTH / 2):
            if self.cur_health <= (MAX_HEALTH / 4):
                pygame.draw.rect(
                    self.game.screen, RED, ((WIN_WIDTH // 2) + 85, 50, self.cur_health / self.health_ratio, 25)
                )
            else:
                pygame.draw.rect(
                    self.game.screen, YELLOW, ((WIN_WIDTH // 2) + 85, 50, self.cur_health / self.health_ratio, 25)
                )
        else:
            pygame.draw.rect(
                self.game.screen, GREEN, ((WIN_WIDTH // 2) + 85, 50, self.cur_health / self.health_ratio, 25)
            )
        pygame.draw.rect(self.game.screen, WHITE, ((WIN_WIDTH // 2) + 85, 50, self.healthbar_length, 25), 2)

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            self.get_damage(10)

    def collide_player(self):
        hits = pygame.sprite.spritecollide(self, self.game.player_group, False)
        if self.vel.x > 0:
            if hits:
                if self.pos.x < self.rect.right:
                    self.pos.x = self.rect.left
                    self.vel.x = 0

        if self.vel.x < 0:
            if hits:
                if self.pos.x > self.rect.left:
                    self.pos.x = self.rect.right
                    self.vel.x = 0

    def animate_death(self):
        death_animation = [
            self.game.fixer_sprite_sheet.get_sprite(13, 1078, 122, 116),
            self.game.fixer_sprite_sheet.get_sprite(147, 1079, 122, 116),
            self.game.fixer_sprite_sheet.get_sprite(284, 1086, 122, 122),
            self.game.fixer_sprite_sheet.get_sprite(418, 1105, 152, 83),
        ]

        if self.cur_health == 0:
            self.image = death_animation[math.floor(self.death_frame)]
            self.image.set_colorkey(MAGENTA2)
            self.death_frame += 0.2
            if self.death_frame >= 4:
                self.death_frame = 0
                self.dead = True
            if self.dead == True:
                self.image = self.game.fixer_sprite_sheet.get_sprite(6, 1208, 198, 63)
                self.image.set_colorkey(MAGENTA2)
                # self.acc = 0

    def character_name(self):
        self.font = pygame.font.Font("resources/fonts/arial.ttf", 32)
        text = self.font.render("The Fixer", True, WHITE)
        text_rect = text.get_rect(x=(WIN_WIDTH // 2) + 250, y=10)
        self.game.screen.blit(text, text_rect)


# import pygame, math
# from pygame.locals import *
# from data.sprite_sheet import *
# from config import *

# # -------------- Player Class ------------------
# class Player2(pygame.sprite.Sprite):
#     def __init__(self, game):
#         self.game = game
#         self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
#         self.image.set_colorkey(MAGENTA)
#         self.rect = self.image.get_rect()
#         self.groups = self.game.all_sprites, self.game.player2_group
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.width = 145
#         self.height = 125

#         # --------------- Position and Direction -------------
#         self.vx = 0
#         self.pos = vec((600, 240))
# self.pos = vec((self.game.sockets.get_player2_x(), 240))
#         self.vel = vec(0, 0)
#         self.acc = vec(0, 0)

#         # -------------- Movement --------------
#         self.direction = "RIGHT"
#         self.jumping = False
#         self.running = False
#         self.move_frame = 0
#         self.run_ani_R = [
#             self.game.alucard_sprite_sheet.get_sprite(268, 795, self.width, self.height),
#             self.game.alucard_sprite_sheet.get_sprite(75, 793, self.width, self.height),
#             self.game.alucard_sprite_sheet.get_sprite(54, 927, self.width, self.height),
#         ]

#         self.run_ani_L = [
#             self.game.alucard_sprite_sheet.get_sprite(268, 795, self.width, self.height),
#             self.game.alucard_sprite_sheet.get_sprite(75, 793, self.width, self.height),
#             self.game.alucard_sprite_sheet.get_sprite(54, 927, self.width, self.height),
#         ]

#         # ----------- Combat ---------------------
#         self.attacking = False
#         self.cooldown = False
#         self.attack_frame = 0
#         self.attack_ani_R = [
#             self.game.alucard_sprite_sheet.get_sprite(30, 3866, self.width, self.height - 25),
#             self.game.alucard_sprite_sheet.get_sprite(170, 3866, self.width, self.height - 25),
#             self.game.alucard_sprite_sheet.get_sprite(314, 3860, self.width + 55, self.height),
#         ]

#         self.attack_ani_L = [
#             self.game.alucard_sprite_sheet.get_sprite(30, 3866, self.width, self.height - 25),
#             self.game.alucard_sprite_sheet.get_sprite(170, 3866, self.width, self.height - 25),
#             self.game.alucard_sprite_sheet.get_sprite(314, 3860, self.width + 55, self.height),
#         ]

#     def move(self):
#         self.acc = vec(0, 0.5)
#         if abs(self.vel.x) > 0.3:
#             self.running = True
#         else:
#             self.running = False

#         # opponent_move = self.game.sockets.get_opponent_move()
#         # --------- keyboard input ----------------
#         pressed_keys = pygame.key.get_pressed()
#         if pressed_keys[K_a]:
#         # if opponent_move == "left":
#             self.acc.x = -ACC
#             self.direction = "LEFT"
#             # self.game.sockets.reset_opponent_move()
#         # if opponent_move == "right":
#         if pressed_keys[K_s]:
#             self.acc.x = ACC
#             self.direction = "RIGHT"
#             # self.game.sockets.reset_opponent_move()
#         # if opponent_move == "jump":
#             # self.jump()
#             # self.game.sockets.reset_opponent_move()
#         # if opponent_move == "attack":
#             # self.attack()
#             # self.game.sockets.reset_opponent_move()

#         self.acc.x += self.vel.x * FRIC
#         self.vel += self.acc
#         self.pos += self.vel + 0.5 * self.acc

#         if self.pos.x > WIN_WIDTH:
#             self.pos.x = 0
#         if self.pos.x < 0:
#             self.pos.x = WIN_WIDTH
#         self.rect.midbottom = self.pos

#     def gravity_check(self):
#         # hits = collide with anything in the ground_group
#         hits = pygame.sprite.spritecollide(self, self.game.ground_group, False)
#         if self.vel.y > 0:
#             if hits:
#                 lowest = hits[0]
#                 if self.pos.y < lowest.rect.bottom:
#                     self.pos.y = lowest.rect.top + 1
#                     self.vel.y = 0
#                     self.jumping = False

#     # ---------- method calls -----------
#     def update(self):
#         self.move()
#         self.gravity_check()
#         self.animate()

#     def animate(self):
#         if self.move_frame > 3:
#             self.move_frame = 0
#             return

#         if self.jumping == False and self.running == True:
#             if self.vel.x > 0:
#                 if self.direction == "RIGHT" and self.running is False:
#                     self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
#                     self.image.set_colorkey(MAGENTA)
#                 else:
#                     self.image = self.run_ani_R[math.floor(self.move_frame)]
#                     self.image.set_colorkey(MAGENTA)
#             elif self.vel.x < 0:
#                 if self.direction == "LEFT" and self.running is False:
#                     self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
#                     self.image = pygame.transform.flip(self.image, True, False)
#                     self.image.set_colorkey(MAGENTA)
#                 else:
#                     self.image = self.run_ani_L[math.floor(self.move_frame)]
#                     self.image.set_colorkey(MAGENTA)
#                     self.image = pygame.transform.flip(self.image, True, False)

#             self.move_frame += 0.1

#         if abs(self.vel.x) < 0.2 and self.move_frame != 0:
#             self.move_frame = 0
#             if self.direction == "RIGHT":
#                 self.image = self.run_ani_R[self.move_frame]
#             elif self.direction == "LEFT":
#                 self.image = self.run_ani_L[self.move_frame]

#     # ----- correction for pygame attack error when attacking left ----------
#     def correction(self):
#         if self.attack_frame == 1:
#             self.pos.x -= 20
#         if self.attack_frame == 4:
#             self.pos.x += 20

#     def attack(self):
#         if self.attack_frame > 3:
#             self.attack_frame = 0
#             self.attacking = False

#         if self.direction == "RIGHT":
#             self.image = self.attack_ani_R[math.floor(self.attack_frame)]
#             self.image.set_colorkey(MAGENTA)
#         elif self.direction == "LEFT":
#             self.correction()
#             self.image = self.attack_ani_L[math.floor(self.attack_frame)]
#             self.image.set_colorkey(MAGENTA)
#             self.image = pygame.transform.flip(self.image, True, False)
#         self.attack_frame += 0.3

#     # def player_hit(self):
#     #     hits = pygame.sprite.spritecollide(self, self.player, False)
#     #     if self.cooldown == False:
#     #         self.cooldown = True
#     #         pygame.time.set_timer(self.hit_cooldown, 1000)

#     #         pygame.display.update()

#     def jump(self):
#         self.rect.x += 1
#         hits = pygame.sprite.spritecollide(self, self.game.ground_group, False)

#         self.rect.x -= 1

#         if hits and not self.jumping:
#             self.jumping = True
#             self.vel.y = -12
