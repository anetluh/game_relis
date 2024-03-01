''''    from pygame import *
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
            if keys_pressed[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed

            if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
                self.rect.x += self.speed     

    class Player2(GameSprite):
        def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_d] and self.rect.x > 5:
                self.rect.x -= self.speed

            if keys_pressed[K_a] and self.rect.x < win_width - 80:
                self.rect.x += self.speed             

    class Enemy(GameSprite):
        def update(self):
            self.rect.y += self.speed
            global lost 

            if self.rect.y > win_height:
                self.rect.x = randint(80, win_width - 80)
                self.rect.y = 0
                lost = lost + 1
    #лічильник зловлених та пропущених яєць для Першого гравця
        
    score1 = 0
    #lost1 = 0   

    #лічильник зловлених та пропущених яєць для Другого гравця
        
    score2 = 0
    #lost2 = 0  

    #ігрова сцена         
    window = display.set_mode((800, 500))
    win_width = 800
    win_height = 500
    window = display.set_mode((win_width, win_height))
    display.set_caption("Wolf Game")
    background = transform.scale(image.load("Fon.png"),(win_width, win_height))

    #шрифти
    font.init()
    font1 = font.Font(None, 80)
    font1 = font.Font(None, 36)

    txt_lose_game1 = font1.render('WIN PLAYER 1', True, [255, 0, 0])
    txt_win_game1 = font1.render('YOU WIN', True, [0, 255, 0])


    font.init()
    font2 = font.Font(None, 80)
    font2 = font.Font(None, 36)

    txt_lose_game2 = font2.render('WIN PLAYER 2', True, [255, 0, 0])
    txt_win_game2 = font2.render('YOU WIN', True, [0, 255, 0])


    #спрайти
    wolf1 = "wolf_2001.png"
    wolf2= "wolf_2002.png"
    game_fon = "Fon.png"
    egg = "egg.png"


    wolf1 = Player1("wolf_2001.png", 13, win_height - -40, 400, 80, 100)
    wolf2 = Player2("wolf_2002.png", 13, win_height - 325, 400, 80, 100)
    # bullets = sprite.Group()
    # monsters = sprite.Group()
    # for i in range(1, 5):
    #     monster = Enemy(ufo, randint(1, 5),randint(80, win_width - 80), -35, 80, 50)
    #     monsters.add(monster)




    # змінна гра закінчилась

    # finish = False

    # основний цикл
    run = True

    while run:
    
        for e in event.get():
            if e.type == QUIT:
                run = False

        window.blit(background, (0, 0))  

        wolf1.update()
        wolf1.update()
        wolf1.recet()

        wolf2.update()
        wolf2.update()
        wolf2.recet()
        
        display.update()
        
        time.delay(50)
''''

