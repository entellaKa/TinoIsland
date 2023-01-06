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
play = False

bg = pygame.image.load("images/background/backgroundPixel01.jpg")
bg = pygame.transform.scale(bg, (900, 450))
print(bg.get_width(), bg.get_height())

characterImageAddress = [['images/entity/character01_front01.png', 'images/entity/character01_front02.png',
                          'images/entity/character01_front03.png', 'images/entity/character01_front04.png'],
                         ['images/entity/character01_back01.png', 'images/entity/character01_back02.png',
                          'images/entity/character01_back03.png', 'images/entity/character01_back04.png'],
                         ['images/entity/character01_right01.png', 'images/entity/character01_right02.png',
                          'images/entity/character01_right03.png', 'images/entity/character01_right04.png'],
                         ['images/entity/character01_left01.png', 'images/entity/character01_left02.png',
                          'images/entity/character01_left03.png', 'images/entity/character01_left04.png']]
images = []
for j in range(4):
    img = [pygame.transform.scale(pygame.image.load(i), (60, 45)) for i in characterImageAddress[j]]
    images.append(img)

#print(map.map)


def runGame():
    global done, images, play
    x = 200
    y = 200
    characterKey = 0
    character = images[characterKey]

    n = 0
    while not done:
        clock.tick(10)
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            n = 0
            if event.type == pygame.KEYDOWN:
                play = True
                if event.key == pygame.K_DOWN:
                    characterKey = 0
                elif event.key == pygame.K_UP:
                    characterKey = 1
                elif event.key == pygame.K_RIGHT:
                    characterKey = 2
                elif event.key == pygame.K_LEFT:
                    characterKey = 3
                elif event.key == pygame.K_ESCAPE:
                    done = True
                character = images[characterKey]
            elif event.type == pygame.KEYUP:
                play = False
            #     if event.key == pygame.K_DOWN:
            #         characterKey = 0
            #     elif event.key == pygame.K_UP:
            #         characterKey = 1
            #     elif event.key == pygame.K_RIGHT:
            #         characterKey = 2
            #     elif event.key == pygame.K_LEFT:
            #         characterKey = 3
            elif event.type == pygame.QUIT:
                done = True

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and map.map1[y//20][(x+45+5)//30] == 1:
            x += 5
        if key[pygame.K_LEFT] and map.map1[y//20][(x-5)//30] == 1:
            x -= 5
        if key[pygame.K_DOWN] and map.map1[(y+5)//20][x//30] == 1:
            y += 5
        if key[pygame.K_UP] and map.map1[(y-5)//20][x//30] == 1:
            y -= 5

        if play:
            n += 1
        screen.blit(bg, (0, 0))
        screen.blit(character[n % 4], (x, y))
        pygame.display.update()


runGame()
pygame.quit()
