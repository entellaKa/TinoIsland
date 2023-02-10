import pygame, time

pygame.init()

screen = pygame.display.set_mode((900, 450))
pygame.display.set_caption("tino Island")

clock = pygame.time.Clock()


# screen.fill((255, 255, 255))
# time.sleep(5)
# pygame.display.update()
# screen.fill((0, 255, 255))
# time.sleep(5)
# pygame.display.update()
# screen.fill((255, 0, 255))
# time.sleep(5)
# pygame.display.update()
# screen.fill((255, 255, 0))
# time.sleep(5)
# pygame.display.update()

colors = [(255,255,255),(155,0,155),(255,255,0)]
    

def play():
    color = colors[0]
    i = 0
    done = True

    while done:
        clock.tick(500)
        screen.fill(color)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                i+=1
                color = colors[i%len(colors)]
            elif event.type == pygame.QUIT:
                done = False
        print("wake up!",i)

play()
pygame.quit()
