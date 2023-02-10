import pygame
import os, getpass

name = getpass.getuser()
os.chdir("C:/Users/"+name+"/Desktop/Ka/Programing/Python/game/tino_island")

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

direction = 0 #0 정면, 1후면, 2우측, 3좌측

moving = False

pos_x = 200
pos_y = 200

n = 0

def move(x, y, dir = 0):
    global pos_x, pos_y, n
    pos_x += x
    pos_y += y
    direction = dir
    image = images[direction]

    if moving:
        n+=1
    return image[n%4]

def get_pos():
    return (pos_x, pos_y)

    