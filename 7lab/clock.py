import pygame  
import datetime  
import os  
import math  

# Setting up the center and radius of the clock
center = (250, 250)
clock_radius = 250

# Initializing Pygame
pygame.init()

# Creating the game window
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()  # Creating a clock object for setting the frame rate

# Loading the Mickey Mouse background image
mickey = pygame.image.load(r'mickey.jpg')
mickey = pygame.transform.scale(mickey, (500, 500))  # Scaling the image to fit the window

# Loading the clock hand images and setting their positions
handmin = pygame.image.load(r'minhand.png')
handmin = pygame.transform.scale(handmin, (200, 300))
handmin_rect = handmin.get_rect()
handmin_rect.center = (250, 250)  # Setting the center position of the minute hand

handsec = pygame.image.load(r'sechand.png')
handsec = pygame.transform.scale(handsec, (200, 270))
handsec_rect = handsec.get_rect()
handsec_rect.center = (250, 250)  # Setting the center position of the second hand

# Defining the game loop
def game():
    while True:
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()  # Exiting the program if the user clicks the close button
                
        # Getting the current time
        now = datetime.datetime.now()
        second = now.second
        minute = now.minute
        hour = now.hour
        
        # Clearing the screen and drawing the clock face
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 255), center, 10)
        pygame.draw.circle(screen, (255, 255, 255), center, 10)
        
        # Blitting the Mickey Mouse background image onto the screen
        screen.blit(mickey, (0, 0))
        
        # Rotating and blitting the minute hand onto the screen
        rot_handmin = pygame.transform.rotate(handmin, (-1*(6*minute) - 360))  # Rotating the image based on the current minute
        rot_handmin_rect = rot_handmin.get_rect()
        rot_handmin_rect.center = handmin_rect.center  # Setting the center position of the rotated image to the center position of the original image
        screen.blit(rot_handmin, rot_handmin_rect)
        
        # Rotating and blitting the second hand onto the screen
        rot_handsec = pygame.transform.rotate(handsec, (-1*(6*second)))  # Rotating the image based on the current second
        rot_handsec_rect = rot_handsec.get_rect()
        rot_handsec_rect.center = handsec_rect.center  # Setting the center position of the rotated image to the center position of the original image
        screen.blit(rot_handsec, rot_handsec_rect)
        
        # Updating the screen and setting the frame rate to 60 fps
        pygame.display.flip()
        clock.tick(60)

# Calling the game loop function to start the program
game()