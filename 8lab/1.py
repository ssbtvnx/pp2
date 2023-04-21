import pygame

# Load the image
my_image = pygame.image.load('coin.png')

# Get the rectangle area of the image
rect = my_image.get_rect()

# Print the position and dimensions of the rectangle
print(rect.x, rect.y, rect.width, rect.height)
