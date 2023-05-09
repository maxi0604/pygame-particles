# import the pygame module, so you can use it
import pygame
import random
import math
import numpy as np


def llerp(a, b, t):
    t = min(1, max(0, t))
    return (1 - t) * a + t * b


def get_color(x):
    rhot, ghot, bhot = (245, 40, 40)
    rmid, gmid, bmid = (40, 245, 40)
    rcld, gcld, bcld = (40, 40, 245)
    if x <= 0.5:
        rres, gres, bres = llerp(
            rcld, rmid, 2 * x), llerp(gcld, gmid, 2 * x), llerp(bcld, bmid, 2 * x)
    else:
        rres, gres, bres = llerp(
            rmid, rhot, 2 * x - 1), llerp(gmid, ghot, 2 * x - 1), llerp(bmid, bhot, 2 * x - 1)
    # value = min(255, max(0, x * 255))
    # return (value, value, value)
    return (rres, gres, bres)
# define a main function

def do_step(world, world_next, width, height):
    sum = 0
    alpha = 1/5
    for x in range(width):
        for y in range(height):
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)]
            delta = 0
            for dx, dy in offsets:
                beta = 1
                if dx != 0 and dy != 0:
                    beta = 0.707
                ox, oy = x + dx, y + dy
                if not (0 <= ox < width and 0 <= oy < height):
                    continue
                delta += beta * (world[ox][oy] - world[x][y])

            world_next[x][y] = world[x][y] + alpha * delta

            sum += world_next[x][y]
    return sum
def main():
    width, height = 300, 200
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("Particle simulation.")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    # define a variable to control the main loop
    running = True

    # world = [[0 for j in range(height)] for j in range(width)]
    # world_next = [[0 for j in range(height)] for j in range(width)]
    world = np.zeros((width, height))
    world_next = np.zeros((width, height))
    for i in range(width // 2):
        for j in range(height):
            if i < j:
                world[i][j] = 1
    # main loop
    fcount = 0
    while running:
        fcount += 1
        # dt = clock.tick(240)

        (mouse_left, mouse_mid, mouse_right) = pygame.mouse.get_pressed(num_buttons=3)
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        if mouse_left:
            world[mouse_x][mouse_y] = 10
        elif mouse_right:
            world[mouse_x][mouse_y] = 0

        do_step(world, world_next, width, height)
        for x in range(width):
            for y in range(height):
                screen.set_at((x, y), get_color(world_next[x][y]))
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        if fcount % 1 == 0:
            pygame.display.flip()
        # print(sum)
        world_next, world = world, world_next


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
