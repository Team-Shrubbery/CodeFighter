import pygame

class Button:
    # pass in location of button, size of box, foreground and background color, content and t he fontsize
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font("resources/fonts/arial.ttf", fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        # render font with content(text we want to write), anti aliasing and the foreground color
        self.text = self.font.render(self.content, True, self.fg)
        # position of text, middle of button
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        # render text and rectangle
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        # get position of mouse
        if self.rect.collidepoint(pos):
            # return true if mouse button clicked
            if pressed[0]:
                return True
            return False
        return False 