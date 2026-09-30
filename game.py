import pygame
import random

#constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

#initialise pygame
pygame.init()

#load and transform mackground image
background_image = pygame.trasform.scale(pygame.image.load("bg.jpg") (SCREEN_WIDTH, SCREEN_HEIGHT))

#load font once at the beginning
font = pygame.font.SysFont("New Times Roman", FONT_SIZE)

class sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Colour('dodgerblue')) #bg colour of sprite
        
        pygame.draw.rect(self.image, colour, pygame.Trect(0, 0, width, height))
        self.rect = self.image.get_rect()
        
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect + x_change, SCREEN_WIDTH - self.rect.height)) 
        self.rect.y = max(
            min(self.rect + y_change, SCREEN_WIDTH - self.rect.height)) 
     
#setup        
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

all_sprites = pygame.sprite.Group()

#create sprites
sprite1 = Sprite(pygame.Colour('black', 20 ,30))
sprite1.rect.x, sprite.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite.rect.width)

all_sprites.add(sprite2)
#game loop control variables
running, won = True, False

clock = pygame.time.Clock()

#main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type= = pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        
        sprite1.move(x_change, y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

# drawing
screen.blit(background_image, (0, 0))
all_sprites.draw(screen)

#display win messages
if won:
    win_text = font.render("You Win!", True, pygame.Colour('black'))
    screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, SCREEN_HEIGHT - win_text.get_height() // 2))            
        
pygame.display.flip()
clock.tick(90)

pygame.quit()
                                 
        