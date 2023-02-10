import pygame, mapList, inventory, player, stage00
import os, getpass, subprocess

name = getpass.getuser()
os.chdir("C:/Users/"+name+"/Desktop/Ka/Programing/Python/game/tino_island")


def runGame():
    player.pos_y = 650
        
    pygame.init()

    WHITE = (255, 255, 255)
    SKY_BLUE = (52, 168, 255)
    size = [900, 750]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('tino island')

    done = False
    clock = pygame.time.Clock()

    bg = pygame.image.load("images/background/backgroundPixel02.jpg")
    bg = pygame.transform.scale(bg, (900, 750))

    map1 = mapList.map2
    character = player.move(0,0)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = not done
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    inventory.inventoryOpen = not inventory.inventoryOpen
                    print("inventory")
            elif event.type == pygame.KEYUP:
                player.moving = False
                player.n = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and map1[player.pos_y//20][(player.pos_x+45+5)//30] == 0:
            character = player.move(5, 0, 2)
            player.moving = True

        elif key[pygame.K_LEFT] and map1[player.pos_y//20][(player.pos_x-5)//30] == 0:
            character = player.move(-5, 0, 3)
            player.moving = True

        if key[pygame.K_DOWN] and map1[(player.pos_y+5)//20][player.pos_x//30] == 0:
            character = player.move(0, 5, 0)
            player.moving = True

        elif key[pygame.K_UP] and map1[(player.pos_y-5)//20][player.pos_x//30] == 0:
            character = player.move(0, -5, 1)
            player.moving = True
        
        if map1[player.pos_y//20+1][player.pos_x//30] == 3:
            # curMap = mapList.map2
            done = not done
            player.pos_y = 40
            pygame.quit()

            stage00.runGame()
            # stage00.runGame()

        screen.blit(bg, (0, 0))

        screen.blit(character, (player.pos_x, player.pos_y))

        if inventory.inventoryOpen:
            inventory.draw_inventory(screen)


        pygame.display.flip()
        pygame.display.update()

        clock.tick(25)