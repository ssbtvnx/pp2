import pygame
from random import randrange
import time
import datetime

pygame.init()

size=30
square=20*size

x,y=randrange(0, square, size ), randrange(0, square, size)
food=randrange(0, square, size), randrange(0, square, size)
food1 = randrange(0, square, size), randrange(0, square, size)
length=1
snake=[(x, y)]
dx,dy=0, 0
FPS=6
score=0
level=1
smth={'UP':True, 'DOWN':True, 'RIGHT':True, 'LEFT':True}

screen = pygame.display.set_mode((square,square))
clock = pygame.time.Clock()
font_score=pygame.font.SysFont('Verdana',26,bold = True)
font_end=pygame.font.SysFont('Verdana',66,bold = True)

# timer for food
food_timer = pygame.USEREVENT+1

def food_disappers(seconds=6):
    pygame.time.set_timer(food_timer, seconds*1000)


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


while True:
    screen.fill(pygame.Color('black'))
    #drawing snake, food
    [pygame.draw.rect(screen, pygame.Color('green'), (i, j, size-2, size-2)) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*food, size, size))
    pygame.draw.rect(screen,pygame.Color('orange'),(*food1, size, size))
    
    #show score, level
    render_score=font_score.render(f'Score:{score}', 1,pygame.Color('blue'))
    screen.blit(render_score,(5,5))
    render_level=font_score.render(f'Level:{level}', 1,pygame.Color('blue'))
    screen.blit(render_level, (size*15, 5))
    
    #snake movement
    x+=dx*size
    y+=dy*size 
    snake.append((x,y))
    snake=snake[-length:]

    
    #eating food
    if snake[-1]==food:
        food=randrange(0,square,size) , randrange(0,square,size)
        length+=1
        score+=1
    elif snake[-1]==food1:
        food1=randrange(0, square, size), randrange(0, square, size)
        length+=2
        score+=1
        if score%3==0:
            level+=1
            FPS+=2 
    

    #game over
    if x<0 or x>square-size or y<-1 or y>square-size or len(snake)!=len(set(snake)):
        while True:
            render_end=font_end.render('Game over!',1,pygame.Color('blue'))
            screen.blit(render_end,(square//2-190, square//2.5 ))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(FPS)
    food_disappers()
    close_game()

    #controls
    key=pygame.key.get_pressed()
    if key[pygame.K_UP] and smth['UP']:
        dx,dy=0,-1 
        smth={'UP':True, 'DOWN':False, 'RIGHT':True, 'LEFT':True}
    elif key[pygame.K_DOWN] and smth['DOWN']:
        dx,dy=0,+1 
        smth={'UP':False, 'DOWN':True, 'RIGHT':True, 'LEFT':True}
    elif key[pygame.K_RIGHT] and smth['RIGHT']:
        dx,dy=+1,0 
        smth={'UP':True, 'DOWN':True, 'RIGHT':True, 'LEFT':False}
    elif key[pygame.K_LEFT] and smth['LEFT']:
        dx,dy=-1,0 
        smth={'UP':True, 'DOWN':True, 'RIGHT':False, 'LEFT':True}