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

    def setPosition( self, position ):
        self.position = position 

    def draw(self):
        screen.blit(self.img, self.position)

dakkaHouse = House('house.png', (100,100), (400, 200))

x = 0
y = 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")   

    x = x + 1
    dakkaHouse.setPosition((x, y))

    dakkaHouse.draw()

    pygame.display.flip()
    # pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()