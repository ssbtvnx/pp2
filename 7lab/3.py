import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

x = 30
y = 30
clock=pygame.time.Clock()

#отслеживает событие "закрыть окно"
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()
        
        pressed = pygame.key.get_pressed() #для получения текущее состояние всех клавиш клавиатуры
        if pressed[pygame.K_UP] and y-20>11: y -= 20
        if pressed[pygame.K_DOWN] and y+20<280: y += 20
        if pressed[pygame.K_LEFT] and x-20>13: x -= 20
        if pressed[pygame.K_RIGHT] and x+20<380: x += 20
        screen.fill((255,255,255)) #заполняем всю поверхность окна белым
        color = (255, 0, 0)
        pygame.draw.circle(screen, color,(x,y), 25) #рисует круг
        
        pygame.display.flip()
        clock.tick(60) #ограничивает частоту кадров