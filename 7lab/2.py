import pygame
import os

path = r'C:\Users\user\Documents\album.jpg'
photo = pygame.image.load(path) #загружает изображение
#координаты
photox = 1
photoy = 1

def image():
    screen.blit(photo, (photox, photoy)) #отрисовывает изображение

path2 = r'C:\Users\user\Documents\album'
album = os.listdir(path2) #создаем список всех файлов в этой папке
song_index = 0

def play_music():
    pygame.mixer.music.load(os.path.join(path2, album[song_index])) 
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global song_index
    song_index = (song_index + 1) % len(album)
    play_music()

def prev_music():
    global song_index
    song_index = (song_index - 1) % len(album)
    play_music()

pygame.init() #инициализирует все модули pygame
screen = pygame.display.set_mode((530, 530)) #создает окно 

clock = pygame.time.Clock()

#отслеживает событие "закрыть окно"
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit() 
        if event.type == pygame.KEYDOWN: #проверка: была ли нажата клавиша
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy(): #проверка: воспроизводиться ли музыка 
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()
            
    
    screen.fill((255, 255, 255))
    image() 
    pygame.display.flip() #обновляет отображение
    clock.tick(60) #ограничивает частоту кадров