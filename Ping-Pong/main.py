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
            self.direction = "up"
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
            self.direction = "down"

class Ball(GameSprite):
    def update(self):
        pass

Board1 = Player("racket.png", 100, 500, 39, 136, 10)
Board2 = Player("racket.png", 900, 500, 39, 136, 4)
ball = Ball("tenis_ball.png", 500,400,50,50,6)

font.init()

font1 = font.Font(None, 45)
Text2 = font1.render("PLAYER 1 LOOSE", True, (255,0,0))
Text1 = font1.render("PLAYER 2 LOOSE", True, (255,0,0))

ball_speed_x = 5
ball_speed_y = 5

Clocks = time.Clock()
game = True
FPS = 60
finish = False
direction = "up"
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        Board2.rect.y = ball.rect.y
        #Board1.rect.y = ball.rect.y

        if ball.rect.y >= 650 or ball.rect.y <= 0:
            ball_speed_y *= -1

        if sprite.collide_rect(ball, Board1):
            ball_speed_x *= -1
            if Board1.direction == "up" and ball_speed_y < 0:
                ball_speed_y = -12
                ball_speed_x = 8
            elif Board1.direction == "down" and ball_speed_y > 0:
                ball_speed_y = 12
                ball_speed_x = 8
            elif Board1.direction == "down" and ball_speed_y < 0:
                ball_speed_y = 10
                ball_speed_x = 10
            elif Board1.direction == "up" and ball_speed_y > 0:
                ball_speed_y = -10
                ball_speed_x = 10

        if sprite.collide_rect(ball, Board2):
            ball_speed_x *= -1

        if ball.rect.x < 0:
            window.blit(Text2, (400,350))
            finish = True
        if ball.rect.x > 1000:
            window.blit(Text1, (400,350))
            finish = True

        Board1.update_l()
        Board1.reset()
        Board2.reset()
        ball.reset()

    display.update()
    Clocks.tick(FPS)
