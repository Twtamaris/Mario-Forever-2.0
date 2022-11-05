import pygame
pygame.init()

WEIDTH = 800
HEIGHT = int(800 * 0.8)

BG = (144, 201, 120)

# display screen
screen = pygame.display.set_mode((WEIDTH, HEIGHT))
# this will set the caption of the python window
pygame.display.set_caption("MyGame")
# code to take out image
img = pygame.image.load('img/player/Idle/0.png')
# increase size of image
img_multi = pygame.transform.scale(
    img, (img.get_width() * 3, img.get_height() * 3))


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.img = pygame.image.load('img/player/Idle/0.png')
        # increase size of image
        self.img_multi = pygame.transform.scale(
            img, (img.get_width() * 3, img.get_height() * 3))
        # get rectangle of transformed image
        self.rect = self.img_multi.get_rect()
        self.rect.center = (x, y)

        print(self.rect.center)

    def draw(self):
        screen.blit(self.img_multi, self.rect.center)


ram = Soldier(0, 0)
shyam = Soldier(200, 200)

run = True
while run:
    ram.draw()
    shyam.draw()

    # pygame event handler
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            run = False
        # key down event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
