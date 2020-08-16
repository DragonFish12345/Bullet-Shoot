import pygame

# Creating window
window = pygame.display.set_mode((800, 600))

# Setting up the window
icon = pygame.image.load('logo1.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Bullet Shoot')

# While loop
running = True

# Characters:

# Red Rectangle
redrectstats = redrectx, redrecty, redrectl, redrectw = (0, 0, 50, 50)

# Cyan Rectangle
cyanrectstats = cyanrectx, cyanrecty, cyanrectl, cyanrectw = (750, 0, 50, 50)

# Bullet
bulletstats = bulletx, bullety = (25, 25)
bulletr = 20
def shoot():
        bullet = pygame.draw.circle(window, (255, 255, 255), bulletstats, bulletr)

# Loading explosion
explosion = pygame.image.load('explosion.png')
def explode():
    window.fill((0, 0, 0))
    window.blit(explosion, (100, 100))

while running:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redrect = pygame.draw.rect(window, (255, 0, 0), redrectstats)
    cyanrect = pygame.draw.rect(window, (0, 255, 255), cyanrectstats)
    bulletstats = bulletx, bullety

    shoot()
    # Creating Key Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
    # Updating bullet position
        if bulletx < 750:
            bulletx += 1
        else:
            explode()
    if bulletx >= 750:
        explode()

    pygame.display.update()



