import pygame, math
from pygame.locals import *
from data.sprite_sheet import *
from config import *

# -------------- Player Class ------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
        self.image.set_colorkey(MAGENTA)
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites, self.game.player
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.width = 145
        self.height = 125

# --------------- Position and Direction -------------
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

# -------------- Movement --------------
        self.direction = "RIGHT"
        self.jumping = False
        self.running = False
        self.move_frame = 0
        self.run_ani_R = [self.game.alucard_sprite_sheet.get_sprite(268, 795, self.width, self.height), self.game.alucard_sprite_sheet.get_sprite(75, 793, self.width, self.height),
        self.game.alucard_sprite_sheet.get_sprite(54, 927, self.width, self.height)]

        self.run_ani_L = [self.game.alucard_sprite_sheet.get_sprite(268, 795, self.width, self.height), self.game.alucard_sprite_sheet.get_sprite(75, 793, self.width, self.height),
        self.game.alucard_sprite_sheet.get_sprite(54, 927, self.width, self.height)]


# ----------- Combat ---------------------
        self.attacking = False
        self.cooldown = False
        self.attack_frame = 0
        self.attack_ani_R = [self.game.alucard_sprite_sheet.get_sprite(30, 3866, self.width, self.height - 25),
                            self.game.alucard_sprite_sheet.get_sprite(170, 3866, self.width, self.height - 25),
                            self.game.alucard_sprite_sheet.get_sprite(314, 3860, self.width + 55, self.height),]
 
        self.attack_ani_L = [self.game.alucard_sprite_sheet.get_sprite(30, 3866, self.width, self.height - 25),
                            self.game.alucard_sprite_sheet.get_sprite(170, 3866, self.width, self.height - 25),
                            self.game.alucard_sprite_sheet.get_sprite(314, 3860, self.width + 55, self.height),]

    def move(self):
        self.acc = vec(0, 0.5)
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

# --------- keyboard input ----------------
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.direction = "LEFT"
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.direction = "RIGHT"
        if pressed_keys[K_SPACE]:
            self.jump()
        if pressed_keys[K_RETURN]:
            self.attack()

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        self.rect.midbottom = self.pos

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
        self.move()
        self.gravity_check()
        self.animate()

    def animate(self):
        if self.move_frame > 3:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
              if self.direction == "RIGHT" and self.running is False:
                self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
                self.image.set_colorkey(MAGENTA)
              else:
                self.image = self.run_ani_R[math.floor(self.move_frame)]
                self.image.set_colorkey(MAGENTA)
            elif self.vel.x < 0:
              if self.direction == "LEFT" and self.running is False:
                self.image = self.game.alucard_sprite_sheet.get_sprite(38, 179, 145, 125)
                self.image = pygame.transform.flip(self.image, True, False)
                self.image.set_colorkey(MAGENTA)
              else:
                self.image = self.run_ani_L[math.floor(self.move_frame)]
                self.image.set_colorkey(MAGENTA)
                self.image = pygame.transform.flip(self.image, True, False)

            self.move_frame += 0.1

        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = self.run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = self.run_ani_L[self.move_frame]

# ----- correction for pygame attack error when attacking left ----------
    def correction(self):
        if self.attack_frame == 1:
            self.pos.x -= 20
        if self.attack_frame == 4:
            self.pos.x += 20


    def attack(self):
        if self.attack_frame > 3:
            self.attack_frame = 0
            self.attacking = False

        if self.direction == "RIGHT":
            self.image = self.attack_ani_R[math.floor(self.attack_frame)]
            self.image.set_colorkey(MAGENTA)
        elif self.direction == "LEFT":
            self.correction()
            self.image = self.attack_ani_L[math.floor(self.attack_frame)]
            self.image.set_colorkey(MAGENTA)
            self.image = pygame.transform.flip(self.image, True, False)
        self.attack_frame += 0.1

    # def player_hit(self):
    #     hits = pygame.sprite.spritecollide(self, self.player, False)
    #     if self.cooldown == False:
    #         self.cooldown = True 
    #         pygame.time.set_timer(self.hit_cooldown, 1000) 

    #         pygame.display.update()

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.ground_group, False)

        self.rect.x -= 1
        
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12
