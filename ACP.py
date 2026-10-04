import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 80

pygame.init()

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height): 
        super().__init__()
        try:
            raw_image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(raw_image, (width, height))
        except (pygame.error, FileNotFoundError):
            self.image = pygame.Surface([width, height])
            self.image.fill(pygame.Color('darkgray')) 
            
        self.rect = self.image.get_rect()
        
    def move(self, x_change, y_change):
        self.rect.x = max(0, min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image.fill(pygame.Color('dodgerblue'))

all_sprites = pygame.sprite.Group()

duck = "duck.jpg" 
sprite1 = Sprite(duck, 40, 40) 
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

pizza = "pizza.jpg" 
sprite2 = Sprite(pizza, 40, 40) 
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
            
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)
        
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
            
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)
    
    if won:
        win_text = font.render("You Win!", True, pygame.Color('black'))
        text_x = (SCREEN_WIDTH - win_text.get_width()) // 2
        text_y = (SCREEN_HEIGHT - win_text.get_height()) // 2
        screen.blit(win_text, (text_x, text_y))
        
    pygame.display.flip()
    clock.tick(90)

pygame.quit()


                                 
        

