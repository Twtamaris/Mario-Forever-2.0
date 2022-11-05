import pygame

pygame.init()

WEIDTH = 800
HEIGHT = int(800 * 0.8)

# display screen
screen = pygame.display.set_mode((WEIDTH, HEIGHT))
pygame.display.set_caption("Fighter")


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        # initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('img/player/Idle/0.png')
        #increase size of image
        self.image = pygame.transform.scale(self.img, (self.img.get_width()* scale, self.img.get_height()* scale))
        #get rectangle of transformed image
        self.image_rect = self.image.get_rect()
        print(self.image_rect)
        self.image_rect.center = (x, y)
        

    def draw(self):
        # display screen

        screen.blit(self.image, self.image_rect)


player1 = Soldier(400, 400, 3)
player2 = Soldier(400, 200, 3)


run = True
# load images using pygame

while run:
    player1.draw()
    player2.draw()
    # pygame event handler
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            run = False
        # key down event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # update display
    pygame.display.update()

pygame.quit()
