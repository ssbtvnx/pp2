import pygame
import random

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up font
font = pygame.font.SysFont(None, 36)

# Set up food variables
foods = []
food_timer = 0
food_duration = 5000  # 5 seconds

# Main game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update food timer
    food_timer += clock.tick(60)
    if food_timer >= 1000:  # 1 second has passed
        food_timer = 0

        # Add a new food if necessary
        if len(foods) < 5:
            foods.append({
                'rect': pygame.Rect(random.randint(0, 640), random.randint(0, 480), 20, 20),
                'spawn_time': pygame.time.get_ticks()
            })

    # Update foods
    for food in foods:
        # Check if food has expired
        if pygame.time.get_ticks() - food['spawn_time'] > food_duration:
            foods.remove(food)

    # Draw screen
    screen.fill(WHITE)

    # Draw foods
    for food in foods:
        pygame.draw.rect(screen, RED, food['rect'])

    # Draw timer
    timer_text = font.render(f"Time: {food_duration - (pygame.time.get_ticks() - foods[0]['spawn_time'])}", True, BLACK)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

# Clean up Pygame
pygame.quit()
