from pygame import*
from random import randint,choice
from time import time as timer

win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('')
background = (200,200,255)
background = transform.scale(image.load('i.webp'),(win_width, win_height))
font.init()
font1 = font.SysFont('Arial',100)
font2 = font.SysFont('Arial',50)
mixer.init()

mixer.music.load('background.mp3')
mixer.music.play()



game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h,hp):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x<900:
            self.rect.x +=self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<650:
            self.rect.y+=self.speed
    def fire(self):
        bullet = Bullet('kit.png',self.rect.centerx,self.rect.top,20,15,20)
        bullets.add(bullet)

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,x,y,width,height):
        super().__init__
        self.image = Surface((width,height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = y
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Enemy(GameSprite):
    def __init__(self,enemy_image,x,y,w,h):
        self.image = transform.scale(image.load(enemy_image),(w,h))
        self.image = Surface((w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy_fire(GameSprite):    
    def update(self):
        global lost
        self.rect.y +=self.speed
        if self.rect.y>win_height:
            self.rect.y = 0
            self.rect.x = randint(80, win_width-80)
        #if self.rect.y>440:
            #touch.play()
class Bullet(GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y<0:
            self.kill()#-----------как удалить с экрана что нибудь
enemy1 = Enemy('elf.png',700,600,50,50,)
enemy2 = Enemy('elf.png',100,600,50,50,)
player = Player('heart.png',300,440,10,50,50,100)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        #if self.rect.x == 595:
            #quest1 = fon1.render('Вы уверены идти дальше?да-1,нет-2')
            #window.blit(quest1, (200,200))

        window.blit(background,(0,0))
        player.reset()
        player.update()
        enemy1.reset()
        enemy1.update()
        enemy2.reset()
        enemy2.update()


    time.delay(20)
    display.update()
