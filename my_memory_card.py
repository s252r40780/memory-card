from pygame import*
from random import randint,choice
from time import time as timer

win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('')
background = (200,200,255)
background = transform.scale(image.load('y.jpg'),(win_width, win_height))
font.init()
font1 = font.SysFont('Arial',100)
font2 = font.SysFont('Arial',50)
mixer.init()

mixer.music.load('background.mp3')
mixer.music.play()
life = 100


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
    def check_collision(self, player_rect, obstacle_rect):
        if player_rect.left < obstacle_rect.right and player_rect.right > obstacle_rect.left and player_rect.top < obstacle_rect.bottom and player_rect.bottom > obstacle_rect.top:
           return True
        return False

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
    obstacle = Rect(200, 200, 100, 100)
    def __init__(self,enemy_image,x,y,w,h):
        self.image = transform.scale(image.load(enemy_image),(w,h))
        #self.image = Surface((w,h))
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
enemy1 = Enemy('elf.png',700,400,75,75,)
enemy2 = Enemy('elf.png',100,600,75,75,)
enemy3 = Enemy('elf.png',850,600,75,75,)
enemy4 = Enemy('elf.png',200,600,75,75,)
enemy5 = Enemy('elf2.png',900,550,115,130,)
player = Player('ii.png',300,440,10,50,50,100)
x = 200
y = 600

player_x = player.rect.x
player_y = player.rect.y
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    player_x = player.rect.x
    player_y = player.rect.y
    
    if not finish:
        if check_collision(player_rect, obstacle_rect):
            player_rect.x = previous_player_x
            player_rect.y = previous_player_y

        
        if player_x == x and player_y == y:
            quest1=font1.render(f"1-спросить где мы 2-спросить как они попали сюда 3- выйти", True, (255, 0, 0))
            window.blit(quest1, (750, 450))
            if keys[K_1]:
                answ1 = font1.render(f'я - Джейкоб и мы сейчас находимся на тропинке к замку, если ты туда идешь то иди на право',True,(255,0,0))
                window.blit(answ1,(750,450))
                quest1.kill()
            if keys[K_2]:
                answ2 = font1.render(f'Меня зовут Джейкоб, и я - эльф. Сегодня вечером я стою с друзьями возле замка на зимней тропинке.
                 Мы собрались здесь, чтобы отпраздновать нашу победу в последней битве против орков.
                Вокруг нас воцарилась тишина, только слабый ветер шепчет свои таинственные истории. 
                Замок выглядит величественно, освещенный лунным светом.
                 Мы смотрим на него с восхищением, чувствуя себя настоящими героями.',True,(255,0,0))
                window.blit(answ2,(750,450))
                quest1.kill()
            elif keys[K_3]:
                quest1.kill()
                answ1.kill()
                answ2.kill()
        if life >=70:
            life_text_color = (0,255,0)    
        if life >=20 and life<70:
            life_text_color = (250,200,50)
        if life <=0 or life<20:
            life_text_color = (255,0,0)     
        if life <=0:
            finish = True
            window.blit(lose,(250,250))
        life_text = font1.render(f'Здоровье:{life}', True ,life_text_color)
        window.blit(life_text,(10,90))
        #if self.rect.x > 595:
            #tropinka = fon1.render('Вы уверены идти дальше?да-9,нет-0')
            #window.blit(quest1, (200,200))

        window.blit(background,(0,0))
        player.reset()
        player.update()
        enemy1.reset()
        enemy1.update()
        enemy2.reset()
        enemy2.update()
        enemy3.reset()
        enemy3.update()
        enemy4.reset()
        enemy4.update()
        enemy5.reset()
        enemy5.update()
    else:
        finish=False
    
    
    time.delay(20)
    display.update()
