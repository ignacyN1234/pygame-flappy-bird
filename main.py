import pygame
import sys
import random

pygame.init()

WIDTH = 1000
HEIGHT = 1000


pygame.display.set_caption("Tekst w pygame")
font = pygame.font.SysFont(None, 36)

text_surface = font.render(  "Hello Pygame!",  True,  (255, 255, 255) )



screen = pygame.display.set_mode((WIDTH , HEIGHT))
SCALE = 4
player_sprite_2 = pygame.image.load('assets/Sprite-0001.png').convert_alpha()
player_sprite = pygame.image.load('assets/sprite3.png').convert_alpha()
obstacle_sprite = pygame.image.load('assets/sprite5.png').convert_alpha()
width_sprite , heigh_sprite  = player_sprite.get_size()
width_sprite2 ,heigh_sprite2 = obstacle_sprite.get_size()
scale_for_obstacle = 30
player_sprite = pygame.transform.scale(player_sprite, (width_sprite * SCALE , heigh_sprite * SCALE ))
player_sprite2 = pygame.transform.scale(player_sprite_2, (width_sprite * SCALE , heigh_sprite * SCALE ))
obstacle_sprite = pygame.transform.scale(obstacle_sprite, (width_sprite2 * scale_for_obstacle , heigh_sprite2 * scale_for_obstacle ))
obstacle_sprite1 = pygame.image.load('assets/sprite1.png').convert_alpha()
obstacle_sprite2 = pygame.image.load('assets/sprite76.png').convert_alpha()

width_sprite3 ,heigh_sprite3 = obstacle_sprite1.get_size()
width_sprite4 ,heigh_sprite4 = obstacle_sprite2.get_size()

obstacle_sprite1 = pygame.transform.scale(obstacle_sprite1, (width_sprite3 * scale_for_obstacle , heigh_sprite3 * scale_for_obstacle ))
obstacle_sprite2 = pygame.transform.scale(obstacle_sprite2, (width_sprite4 * scale_for_obstacle , heigh_sprite4 * scale_for_obstacle ))

WHITE = (255,255,255)
clock = pygame.time.Clock()


class Gracz:
    def __init__(self,pos_x,pos_y):
        # super().__init__()
        self.score = 0
        self.sprites = []
        self.sprites.append(player_sprite)
        self.sprites.append(player_sprite2)
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x , pos_y]
        self.animating = True
        self.acceleration = 0.2
        self.velocityy = 0
        self.skok = False
        self.t = True
        self.game_ended = False
        self.hitbox = self.rect
        self.epstein = True
    def update(self):
        if self.game_ended == False:
            if self.skok == True and self.t == True:
                self.t = False
                self.velocityy = -6

            else:
                self.t = True
                self.acceleration = 0.2
            if self.hitbox.colliderect(Obstacle.hitbox):
                self.game_ended = True
            if self.hitbox.colliderect(Obstacle2.hitbox):
                self.game_ended = True
            self.velocityy += self.acceleration
            self.rect.y += self.velocityy

            if self.animating == True:
                self.current_image += 0.1
                if self.current_image >= len(self.sprites):
                    self.current_image = 0

            if Obstacle2.rect.x < self.rect.y and self.epstein == True:
                self.score += 1
                self.epstein = False
            if Obstacle2.rect.x >= self.rect.y:
                self.epstein = True
            if self.rect.y <= 0 or self.rect.y >= 1000:
                self.game_ended = True
            self.image = self.sprites[int(self.current_image)]

    def draw(self , screen):
        screen.blit(self.image , self.rect)

gracz = Gracz(200,200)

class obstacle1:
    def __init__(self,pos_x,pos_y):
        # super().__init__()


        self.jeffrey = False

        self.image = obstacle_sprite1
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x , pos_y]
        self.rect.y = 300
        self.rect.x = 525
        self.velocityy = -10



        self.hitbox = self.rect.copy()

        self.hitbox.inflate_ip(-650, -450)
        self.hitbox.bottom = self.rect.bottom
        self.rect.bottom = self.hitbox.bottom
        self.hitbox.center = self.rect.center

        self.right = self.hitbox.right
        self.hitbox.width -= 230
        self.hitbox.right = self.right

        self.left = self.rect.left
        self.rect.width -= 80
        self.rect.left = self.left

    def update(self):
        if gracz.game_ended == False:
            self.rect.x += self.velocityy
            if self.rect.x <= -800:
                self.rect.x = 1000
                self.jeffrey = True
            if self.jeffrey == True:
                self.rect.y = random.randint(-50,450)

                self.jeffrey = False
            self.hitbox.center = self.rect.center
            self.hitbox.bottom = self.rect.bottom


    def draw(self,screen):
        screen.blit(self.image , self.rect)
class obstacle2:
    def __init__(self,pos_x,pos_y):





        self.image = obstacle_sprite2
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x , pos_y]
        self.rect.y = Obstacle.rect.y - 400
        self.rect.x = 500
        self.velocityy = -10



        self.hitbox = self.rect.copy()

        self.hitbox.inflate_ip(-650, -400)
        self.hitbox.top = self.rect.top
        self.rect.top = self.hitbox.top
        self.hitbox.center = self.rect.center

        self.right = self.hitbox.right
        self.hitbox.width -= 230
        self.hitbox.right = self.right

        self.left = self.rect.left
        self.rect.width -= 70
        self.rect.left = self.left

    def update(self):
        if gracz.game_ended == False:
            self.rect.x += self.velocityy
            if self.rect.x <= -800:
                self.rect.x = 1000



            self.rect.y = Obstacle.rect.y - 400
            self.hitbox.center = self.rect.center

            self.hitbox.top = self.rect.top

    def draw(self,screen):
        screen.blit(self.image , self.rect)

Obstacle = obstacle1(100,200)
Obstacle2 = obstacle2(100,300)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gracz.skok = True
                gracz.t = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                gracz.skok = False
                gracz.t = False
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    if gracz.game_ended == True:
        print(gracz.score)
        screen.blit(text_surface, (100, 100))
        break
    screen.fill(WHITE)
    #pygame.draw.rect(screen, (0, 0, 255), gracz.rect, 2)
    gracz.update()
    gracz.draw(screen)
    Obstacle.update()
    Obstacle.draw(screen)
    Obstacle2.update()
    Obstacle2.draw(screen)
    #pygame.draw.rect(screen, (255, 0, 255), Obstacle.hitbox, 2)
    #pygame.draw.rect(screen, (255,255, 0), Obstacle2.hitbox, 2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
