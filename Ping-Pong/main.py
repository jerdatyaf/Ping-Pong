from pygame import *
import random

window = display.set_mode((1000, 700))
display.set_caption("Pew Pew")
background = transform.scale(image.load("background.jpg"), (1000, 700))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (player_width,player_height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.width -= 10
        self.rect.height -= 10
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed

Board1 = Player("racket.png", 100, 500, 39, 136, 4)
Board2 = Player("racket.png", 900, 500, 39, 136, 4)

Clocks = time.Clock()
game = True
FPS = 60
while game: # Hi

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))

    Board1.update_l()
    Board2.update_r()
    Board1.reset()
    Board2.reset()

    display.update()
    Clocks.tick(FPS)
