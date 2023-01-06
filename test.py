import pygame
#import map
import map

pygame.init()

WHITE = (255, 255, 255)
SKY_BLUE = (52, 168, 255)
size = [900, 450]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

bg = pygame.image.load("images/background/backgroundPixel01.jpg")
bg = pygame.transform.scale(bg, (900, 450))
print(bg.get_width(), bg.get_height())

character = pygame.transform.scale(pygame.image.load("images/entity/character01_front01.png"), (60, 45))

def runGame():
    global done, character
    x = 3
    y = 15

    while not done:
        clock.tick(10)
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and map.map1[y][x+1] == 1:
            x += 1
        if key[pygame.K_LEFT] and map.map1[y][x-1] == 1:
            x -= 1
        if key[pygame.K_DOWN] and map.map1[y+1][x] == 1:
            y += 1
        if key[pygame.K_UP] and map.map1[y-1][x] == 1:
            y -= 1

        screen.blit(bg, (0, 0))
        screen.blit(character, (x*30, y*20))
        pygame.display.update()


runGame()
pygame.quit()
