import pygame, stage00
import mapList

import os, getpass
os.chdir("C:/Users/"+getpass.getuser()+"/Desktop/Ka/Programing/Python/game/tino_island")

pygame.init()

WHITE = (255, 255, 255)
SKY_BLUE = (52, 168, 255)
size = [900, 450]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tino island')

done = False
clock = pygame.time.Clock()
play = False

font = pygame.font.SysFont("onyx", 40, True, False)
text = font.render("game start", True, (255, 0, 0))
rect = text.get_rect()
rect.centerx = 450
rect.centery = 225

def runGame():
    global done, play, screen, text

    while not done:
        clock.tick(30)
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                pos = pygame.mouse.get_pos()

                if rect.right > pos[0] > rect.left and rect.bottom > pos[1] > rect.top:
                    text = font.render("game start", True, (255, 100, 100))
                    clock.tick(10)
                    pygame.quit()

                    stage00.runGame()
            elif event.type == pygame.QUIT:
                done = True

        screen.blit(text, rect)

        pygame.display.flip()
        pygame.display.update()


runGame()
pygame.quit()
