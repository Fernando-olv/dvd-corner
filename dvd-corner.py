# https://github.com/Tomeczekqq/dvd-corner

from random import randint
import pygame

exit = False

# Settings
SIZE = width, height = 800, 600  # Resolution. (4:3)!
BG_COLOR = (0, 0, 0)  # Background color in RGB
fullscreen = False  # Fullscreen


logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (100, 50))
tint_logo = logo.copy()
clock = pygame.time.Clock()
img_size = logo.get_rect().size
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('DVD Corner')
if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

x = randint(50, width-60)
y = randint(50, height-60)
x_speed = 2.5
y_speed = 2.5

def tint(surf, color):
    """Tint the surface with the given color."""
    tinted_surf = surf.copy()
    tinted_surf.fill(color, special_flags=pygame.BLEND_MULT)
    return tinted_surf

def move(x, y):
    screen.blit(tint_logo, (x, y))


while exit == False:
    screen.fill(BG_COLOR)
    bounced = False
    if (x + img_size[0] >= width) or (x <= 0):
        x_speed = -x_speed
        bounced = True

    if (y + img_size[1] >= height) or (y <= 0):
        y_speed = -y_speed
        bounced = True
    
    x += x_speed
    y += y_speed

    if bounced:
        tint_logo = tint(logo,(randint(50, 255),
         randint(50, 255), randint(50, 255)))

    move(x, y)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

pygame.quit()
