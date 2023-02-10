import pygame, os, getpass

os.chdir("C:/Users/"+getpass.getuser()+"/Desktop/Ka/Programing/Python/game/tino_island")

inventoryOpen = False

width = 160
height = 320

cell_size = 32
 
inventory_window = pygame.Surface((width, height))
inventory_window.fill((200, 200, 200))

item_image = pygame.image.load("images/게임아이콘/식량.png")

inventory = []
# inventory = {}

def add_item(item):
    inventory.append(item)
    # if inventory in item:
    #     inventory[item] += 1
    # else:
    #     inventory[item] = 1

def remove_item(item):
    inventory.remove(item)

def draw_inventory(screen):
    screen.blit(inventory_window, (600, 50)) # 인벤토리 창을 게임 창에 그림


    for i, item in enumerate(inventory):
            inventory_window.blit(item, (5 + (32 * (i // 10)), 5 + (32 * (i % 10))))
    
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(inventory_window, (0, 0, 0), rect, 1)

