import pygame
from random import randrange
import psycopg2 as ps
import pygame_menu
import os

name = input('Enter name: ')

sql_insert = '''
    INSERT INTO snakegame VALUES(DEFAULT, %s, %s, %s);
'''

sql_delete = '''
    DELETE FROM snakegame WHERE name = %s;
'''

sql_show_score = '''
    SELECT name, score, level FROM snakegame
    ORDER BY score DESC;
'''
top = 'TOP PLAYERS (Name, score, level)'

conn = ps.connect(host = 'localhost',
                  database = 'postgres',
                  user = 'postgres',
                  password = 'delete',
                  port = '5432'
)


cur = conn.cursor() #создает курсор который вызывает функции sql

cur.execute(sql_show_score) #для выполнения запросов SQL к базе данных 
hhhh = cur.fetchall() #список кортежей присваивается переменной
pygame.init()


background = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'snakeback.png')), (600, 600))
size=30
square=20*size
screen = pygame.display.set_mode((square,square))
clock = pygame.time.Clock()
font_score=pygame.font.SysFont('Verdana',26,bold = True)
font_end=pygame.font.SysFont('Verdana',66,bold = True)
font_top = pygame.font.SysFont('Verdana', 26, bold = True)
font_table = pygame.font.SysFont('Verdana',15, bold = False)

# timer for food
food_timer = pygame.USEREVENT+1

def food_disappers(seconds=6):
    pygame.time.set_timer(food_timer, seconds*1000)
    
    
def show_score():
    while True:
        diff = 50
        screen.fill(pygame.Color('black'))
        top_render = font_top.render(top, 1, pygame.Color('white')) #  render()создает новую поверхность, содержащую визуализированный текст
        screen.blit(top_render, (50, 5)) #отображает
        mystring = ''
        for i, j in enumerate(hhhh): #возвращает кортеж, содержащий индекс текущей строки и сами данные строки
            mystring = ''
            mystring += str(i+1) #индекс
            mystring += ' '
            mystring += str(j) + ' ' #данные
            table_render = font_table.render(mystring, 1, pygame.Color('white'))
            screen.blit(table_render,(20, diff))
            diff += 20 #чтобы сдвинуть позицию следующей строки таблицы вниз на 20 пикселей
        pygame.display.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cur.close()
                conn.close()
                exit()

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cur.close()
            conn.close()
            exit()

def start_game():
    x,y=randrange(0, square, size ), randrange(0, square, size)
    food=randrange(0, square, size), randrange(0, square, size)
    food1 = randrange(0, square, size), randrange(0, square, size)
    length=1
    global snakegame
    snakegame=[(x, y)]
    dx,dy=0, 0
    FPS=6
    score=0
    level=1
    smth={'UP':True, 'DOWN':True, 'RIGHT':True, 'LEFT':True}
    
    while True:
        screen.fill(pygame.Color('black'))
        #drawing snakegame, food
        [pygame.draw.rect(screen, pygame.Color('green'), (i, j, size-2, size-2)) for i, j in snakegame]
        pygame.draw.rect(screen, pygame.Color('red'), (*food, size, size))
        pygame.draw.rect(screen,pygame.Color('orange'),(*food1, size, size))
    
    #show score, level
        render_score=font_score.render(f'Score:{score}', 1,pygame.Color('blue'))
        screen.blit(render_score,(5,5))
        render_level=font_score.render(f'Level:{level}', 1,pygame.Color('blue'))
        screen.blit(render_level, (size*15, 5))
    
        #snakegame movement
        x+=dx*size
        y+=dy*size 
        snakegame.append((x,y))
        snakegame=snakegame[-length:]

    
    #eating food
        if snakegame[-1]==food:
            food=randrange(0,square,size) , randrange(0,square,size)
            length+=1
            score+=1
        elif snakegame[-1]==food1:
            food1=randrange(0, square, size), randrange(0, square, size)
            length+=2
            score+=1
            if score%3==0:
                level+=1
                FPS+=2

#game over
        if x<0 or x>square or y<-1 or y>square or len(snakegame)!=len(set(snakegame)):
            cur.execute(sql_delete, (name,))
            cur.execute(sql_insert, (name, score, level))
            break
            
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
    

menu = pygame_menu.Menu('snakegame', 400, 300,
                       theme=pygame_menu.themes.THEME_GREEN.set_background_color_opacity(1))

menu.add.button('Play', start_game)
menu.add.button('Scores', show_score)
menu.add.button('Quit', pygame_menu.events.EXIT)


while True:

    screen.blit(background, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            cur.close()
            conn.close()
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)
    
    
    
    pygame.display.update()

    conn.commit()