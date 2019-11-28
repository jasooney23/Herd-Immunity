import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Herd Immunity Simulation")

run = True

random1 = 0
random2 = 0

vaxxCount = 0


font = pygame.font.SysFont('Arial', 20)

simulation = []
vaxx = []

#---------------#
size = 10
immunity = 50
contagion = 50

days = 7
hours = 0

speed = 0.5
#---------------#

hours += 24 * days
currentTime = 0

tick = 0

for y in range(0, size):
    simulation.append([])
    vaxx.append([])
    for x in range(0, size):
        simulation[y].append(False)
        vaxx[y].append(False)

simulation[random.randint(0, size - 1)][random.randint(0, size - 1)] = True

if immunity == 100:
    vaxxCount += 1

while vaxxCount < round(0.01 * immunity * size ** 2):
    random1 = random.randint(0, size - 1)
    random2 = random.randint(0, size - 1)
    if simulation[random1][random2] == True:
        pass
    elif vaxx[random1][random2] == False:
        vaxx[random1][random2] = True
        vaxxCount += 1
        
vaxxCount = 0

def render(grid):
    for y in range(0, grid):
        for x in range(0, grid):
            if vaxx[y][x] == True:
                pygame.draw.circle(screen, (66, 244, 78), \
                    (round((x + 1) * (600 / (grid + 1))), \
                    round((y + 1) * (600 / (grid + 1))) + 100), \
                    round(150 / grid), 0)
            elif simulation[y][x] == True:
                pygame.draw.circle(screen, (244, 98, 66), \
                    (round((x + 1) * (600 / (grid + 1))), \
                    round((y + 1) * (600 / (grid + 1))) + 100), \
                    round(150 / grid), 0)
            else:
                pygame.draw.circle(screen, (66, 192, 244), \
                    (round((x + 1) * (600 / (grid + 1))), \
                    round((y + 1) * (600 / (grid + 1)) + 100)), \
                    round(150 / grid), 0)

def infect(infectious):
    for y in range(0, size):
        for x in range(0, size):
            if simulation[y][x] == True:
                # Surrounding Check
                for q in range(y - 1, y + 2):
                    for p in range(x - 1, x + 2):
                        try:
                            if vaxx[q][p] != True:
                                if random.randint(1, 100) <= infectious:
                                    print("infecting ({0}, {1}) from ({2}, {3})".format(p, q, x, y))
                                    simulation[q][p] = True
                        except:
                            pass

def count(grid, group):
    value = 0
    if group == "infc":
        for y in range(0, grid):
            for x in range(0, grid):
                if simulation[y][x] == True:
                    value += 1
    if group == "safe":
        for y in range(0, grid):
            for x in range(0, grid):
                if simulation[y][x] == False:
                    value += 1
    return value

screen.fill((255, 255, 255))

render(size)
        
info1 = font.render("||  {0} Population  ||  {1}% Immunity  ||  {2}% Contagion Rate  ||"\
    .format(size ** 2, immunity, contagion), False, (0, 0, 0))
info2 = font.render("{0} Days {1} Hours".format(math.floor(currentTime / 24), currentTime - 24 * math.floor(currentTime / 24)), False, (0, 0, 0))
info3 = font.render("||  {0} Infected  ||  {1} Healthy  ||".format(count(size, "infc"), count(size, "safe")), False, (0, 0, 0))

screen.blit(info1, (300 - info1.get_rect().width / 2, 20))
screen.blit(info2, (300 - info2.get_rect().width / 2, 50))
screen.blit(info3, (300 - info3.get_rect().width / 2, 80))

pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if tick >= round(1000 / 16 / speed):
        if currentTime < hours:
            infect(contagion)
            currentTime += 1

        screen.fill((255, 255, 255))

        render(size)
        
        info1 = font.render("||  {0} Population  ||  {1}% Immunity  ||  {2}% Contagion Rate  ||"\
            .format(size ** 2, immunity, contagion), False, (0, 0, 0))
        info2 = font.render("{0} Days {1} Hours".format(math.floor(currentTime / 24), currentTime - 24 * math.floor(currentTime / 24)), False, (0, 0, 0))
        info3 = font.render("||  {0} Infected  ||  {1} Healthy  ||".format(count(size, "infc"), count(size, "safe")), False, (0, 0, 0))

        screen.blit(info1, (300 - info1.get_rect().width / 2, 20))
        screen.blit(info2, (300 - info2.get_rect().width / 2, 50))
        screen.blit(info3, (300 - info3.get_rect().width / 2, 80))

        pygame.display.update()
        tick = 0
        
    tick += 1
    pygame.time.delay(16)

pygame.quit()
