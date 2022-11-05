from pygame import *
import time as t

def restart_pos_ball():
    ball.rect.x = 575
    ball.rect.y = 325

class GameSprite(sprite.Sprite):
    def __init__(self, filename, speedx, speedy, x, y, wh_):
        super().__init__()
        self.image = image.load(filename)
        self.wh_ = wh_
        self.image = transform.scale(
            self.image,
            self.wh_
        )
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,
                    (self.rect.x, self.rect.y)
                    )


class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speedy

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speedy

    def update2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speedy

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speedy

class Button(sprite.Sprite):
    def __init__(self, filename, x, y, wh_):
        super().__init__()
        self.image = image.load(filename)
        self.wh_ = wh_
        self.image = transform.scale(
            self.image,
            self.wh_
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,
                    (self.rect.x, self.rect.y)
                    )

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)



window = display.set_mode((1200, 700))
display.set_caption('PingPong')

background = transform.scale(
    image.load('fon.jpg'),
    (1200, 700)
)

mixer.init()
mixer.music.load('fon_music.ogg')
mixer.music.play()
mixer.music.set_volume(0.008)
cick = mixer.Sound('ball_sound.ogg')

font.init()
font = font.Font(None, 40)

platform1 = Player('platform.png', None, 10, 0, 150, (50, 200))
platform2 = Player('platform2.png', None, 10, 1150, 150, (50, 200))

ball = GameSprite('ball.png', 6, 6, 575, 325, (25, 25))

button_play = Button('button_play.png', 460, 240, (250, 130))
button_exit = Button('button_exit.png', 460, 360, (250, 130))

score_p1 = 0
score_p2 = 0
clock = time.Clock()
FPS = 45
finish = False
game = True
FirstTime = t.time()
while game:


    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button_play.collidepoint(x, y):
                finish = True
            if button_exit.collidepoint(x, y):
                game = False
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                if finish == True:
                    finish = False
                else:
                    finish = True
                    FirstTime = t.time()
                    Timer_s = 0
                    score_p1 = 0
                    score_p2 = 0


    if finish:
        window.blit(
            background, (0, 0)
        )
        SecondTime = t.time()
        Timer_s = SecondTime // 1 - FirstTime // 1

        player1 = font.render(
            'Рахунок:' + str(score_p1), True, (255, 255, 255)
        )
        player2 = font.render(
            'Рахунок:' + str(score_p2), True, (255, 255, 255)
        )
        player1win = font.render(
            'Гравець1 виграв з рахунком ' + str(score_p2) + '-' + str(score_p1), True, (255, 255, 255)
        )
        player2win = font.render(
            'Гравець2 виграв з рахунком ' + str(score_p1) + '-' + str(score_p2), True, (255, 255, 255)
        )
        nobodywin = font.render(
            'Час закінчився', True, (255, 255, 255)
        )
        timer1 = font.render(
            str(Timer_s), True, (255, 255, 255)
        )

        platform1.update1()
        platform1.reset()
        platform2.update2()
        platform2.reset()
        ball.reset()

        ball.rect.x += ball.speedx
        ball.rect.y += ball.speedy


        if ball.rect.y > 675 or ball.rect.y < 0:
            ball.speedy *= -1
            cick.play()

        if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
            ball.speedx *= -1
            cick.play()

        if ball.rect.x >= 1175:
            score_p1 += 1
            restart_pos_ball()

        if ball.rect.x <= 0:
            score_p2 += 1
            restart_pos_ball()

        if score_p1 == 3:
            t.sleep(1)
            window.blit(
                player2win, (365, 50)
            )
            finish = False

        if score_p2 == 3:
            t.sleep(1)
            window.blit(
                player2win, (365, 50)
            )
            finish = False

        if Timer_s >= 60:
            if score_p1 > score_p2:
                window.blit(
                    player2win, (365, 50)
                )
                finish = False
            elif score_p1 < score_p2:
                window.blit(
                    player2win, (365, 50)
                )
                finish = False
            else:
                window.blit(
                    nobodywin, (500, 50)
                )
                finish = False

        window.blit(
            player1, (20, 20)
        )
        window.blit(
            player2, (1050, 20)
        )

        window.blit(
            timer1, (550, 20)
        )
    else:
        button_play.reset()
        button_exit.reset()



    clock.tick(FPS)
    display.update()