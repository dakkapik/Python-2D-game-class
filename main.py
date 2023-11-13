import pygame, os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ASSETS_DIR = './assets'

img = pygame.image.load(os.path.join(ASSETS_DIR, 'house.png'))
img = pygame.transform.scale(img, (100,100))

x = 500
y = 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")   

    # v = s/t

    # p = ds/dt

    # vx =  60 px / 1s

    # vx =  1 px / (1/60)s

    # vy = 1 px / (-2/60)s

    x = x + 1
    y = y - 2


    screen.blit(img, (x, y))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    # pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()