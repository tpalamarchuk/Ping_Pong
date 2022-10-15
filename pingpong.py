#ping_pong
from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, filename, speed, x, y, wh_):
        super().__init__()
        self.image = image.load(filename)
        self.wh_ = wh_
        self.image = transform.scale(
            self.image,
            self.wh_
            )
        self.rect = self.image.get_rect()
        self.speed = speed
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
            self.rect.y += self.speed

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    
    def update2(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

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

font.init()
font = font.Font(None, 45)

platform1 = Player('platform.png', 15, 0, 150, (50, 200))
platform2 = Player('platform2.png', 15, 1150, 150, (50, 200))

ball = GameSprite('ball.png', 20, 575, 325, (25, 25))

clock = time.Clock()
FPS = 30
finish = True
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        window.blit(
            background, (0, 0)
        )
        
    platform1.update1()
    platform1.reset()
    platform2.update2()
    platform2.reset()

    ball.reset()

    clock.tick(FPS)
    display.update()
