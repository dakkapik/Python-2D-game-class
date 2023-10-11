import pygame, os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ASSETS_DIR = './assets'

class House:
    def __init__ (self, imagePath, size, position): 
        img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
        self.img = pygame.transform.scale(img, size)

        self.size = size
        self.position = position
    
    def draw():
        screen.blit(img, self.position)

dakkaHouse = House('house.png', (50,50), (400, 200))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")   

    dakkaHouse.draw()
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    # pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()