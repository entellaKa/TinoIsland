import pygame
import mapList

import os
print("before: %s"%os.getcwd())
os.chdir("C:/Users/Ka/Desktop/Ka/Programing/파이선/game/tino_island")
print("after: %s"%os.getcwd())

pygame.init()

WHITE = (255, 255, 255)
SKY_BLUE = (52, 168, 255)
size = [900, 450]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tino island')

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

#print(mapList.map)

# 인벤토리 창 크기
width = 160
height = 320

cell_size = 32
# 인벤토리 창 생성
inventory_window = pygame.Surface((width, height))
inventory_window.fill((200, 200, 200))
# 인벤토리 창 제목

# 인벤토리 창 배경 색
bg_coelor = (255, 255, 255)

# 아이템 이미지
item_image = pygame.image.load("images/게임아이콘/식량.png")

# 인벤토리 아이템 리스트
inventory = []

# 아이템 추가 함수
def add_item(item):
    inventory.append(item)

def remove_item(item_image):
    inventory.remove(item_image)

inventory_window_open = False

def runGame():
    global done, images, play, inventory_window_open, screen, bg
    pos_x = 200
    pos_y = 200
    curMap = mapList.map1
    characterKey = 0
    character = images[characterKey]

    n = 0
    while not done:
        clock.tick(10)
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            n = 0
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_DOWN:
                #     characterKey = 0
                # elif event.key == pygame.K_UP:
                #     characterKey = 1
                # elif event.key == pygame.K_RIGHT:
                #     characterKey = 2
                # elif event.key == pygame.K_LEFT:
                #     characterKey = 3
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_e:  
                    inventory_window_open = not inventory_window_open
                # 아이템 추가
                elif event.key == pygame.K_SPACE and inventory_window_open:
                    add_item(item_image)
                #아이템 삭제
                elif event.key == pygame.K_BACKSPACE and inventory_window_open:
                    remove_item(item_image)
            elif event.type == pygame.KEYUP:
                    play = False
            elif event.type == pygame.QUIT:
                done = True
        character = images[characterKey]


        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and curMap[pos_y//20][(pos_x+45+5)//30] != 0:
            characterKey = 2
            pos_x += 5
            play = True
        elif key[pygame.K_LEFT] and curMap[pos_y//20][(pos_x-5)//30] != 0:
            characterKey = 3
            pos_x -= 5
            play = True
        if key[pygame.K_DOWN] and curMap[(pos_y+5)//20][pos_x//30] != 0:
            characterKey = 0
            pos_y += 5
            play = True
        elif key[pygame.K_UP] and curMap[(pos_y-5)//20][pos_x//30] != 0:
            characterKey = 1
            pos_y -= 5
            play = True
        if curMap[pos_y//20][pos_x//30] == 2:
            curMap = mapList.map2
            pos_y = 430
            bg = pygame.image.load("images/background/backgroundPixel02.jpg")
            bg = pygame.transform.scale(bg, (900, 900))
            screen = pygame.display.set_mode(900, 900)

        if play:
            n += 1
        screen.blit(bg, (0, 0))
        screen.blit(character[n % 4], (pos_x, pos_y))
                # 인벤토리 창 초기화

        if inventory_window_open:  #인벤토리 창이 열려있으면
            screen.blit(inventory_window, (600, 50)) # 인벤토리 창을 게임 창에 그림

        # 인벤토리에 아이템 출력
        for i, item in enumerate(inventory):
            inventory_window.blit(item, (5 + (32 * (i // 10)), 5 + (32 * (i % 10))))

        for y in range(0, height, cell_size):
            for x in range(0, width, cell_size):
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(inventory_window, (0, 0, 0), rect, 1)

        pygame.display.flip()
        pygame.display.update()


runGame()
pygame.quit()
