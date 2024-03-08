from pygame import *
from random import randint
#звук
mixer.init()
mixer.music.load("muzik_game.mp3")
mixer.music.play()



#зображення
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, width, hight ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > win_width/2:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
              self.rect.x += self.speed  


class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < win_width - 450:
            self.rect.x += self.speed             


        

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global score1 

        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

        if sprite.spritecollide(wolf1, eggs, True):
            score1 += 1


class Enemy1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global score2 

        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

        if sprite.spritecollide(wolf2, eggs, True):
            score2 += 1            
    #лічильник зловлених та пропущених яєць для Першого гравця
        

 #лічильник зловлених та пропущених яєць для Другого гравця
score1 = 0
  
score2 = 0

    #ігрова сцена         
window = display.set_mode((800, 500))
win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Wolf Game")
background = transform.scale(image.load("Fon.png"),(win_width, win_height))

font.init()
#font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

#пишемо текст на екрані

    #спрайти
wolf1 = "wolf_2001.png"
wolf2= "wolf_2002.png"
game_fon = "Fon.png"
egg = "egg.norm(1).png"
egg_bad = "bad_egg.png" 

eggs= sprite.Group()
for i in range(1, 15):
    egg = Enemy("egg.norm(1).png", randint(1, 5),randint(80, win_width - 80), -35, 50, 60)
    eggs.add(egg)

eggs1= sprite.Group()
for i in range(1, 15):
    egg_bad = Enemy("bad_egg.png", randint(1, 5),randint(80, win_width - 80), -35, 50, 60)
    eggs1.add(egg_bad)    


wolf1 = Player1("wolf_2001.png", 13, win_height - -40, 350, 120, 160)
wolf2 = Player2("wolf_2002.png", 13, win_height - 325, 350, 120, 160)

run = True

while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    text = font2.render("Рахунок:"+ str(score1), 1, (36, 36, 143)) 
    text1 = font2.render("Рахунок:"+ str(score2), 1, (36, 36, 143)) 

    window.blit(background, (0, 0))  
    window.blit(text1, (10, 15))
    window.blit(text, (665, 15))

    wolf1.update()
    wolf1.update()
    wolf1.recet()

    wolf2.update()
    wolf2.update()
    wolf2.recet()
    eggs.update()
    eggs.draw(window)
    eggs1.update()
    eggs1.draw(window)


    display.update()
        
    time.delay(50)

