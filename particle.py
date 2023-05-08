# import the pygame module, so you can use it
import pygame, random, math
 
# define a main function
def main():
    width, height = 800, 600 
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("Particle simulation.")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock() 
    # define a variable to control the main loop
    running = True
    
    particles = []
    for i in range(100):
        x, y = random.uniform(0, width), random.uniform(0, height)
        particles.append([x, y])

    print(particles)
    # main loop
    while running:
        dt = clock.tick(60)
        screen.fill((100, 100, 128))
        x_m, y_m = pygame.mouse.get_pos()
        # event handling, gets all event from the event queue
        for i in range(len(particles)):
            part = particles[i]
            part[0] = (part[0] + random.uniform(-1, 1)) % width
            part[1] = (part[1] + random.uniform(-1, 1)) % width
            
            min_dist = math.inf
            snd_min_dist = math.inf
            min_other = None
            snd_min_other = None
            for j in range(i + 1, len(particles)):
                other = particles[j]
                magn = math.hypot(other[0] - part[0], other[1] - part[1])
                if magn == 0:
                    continue

                if magn < min_dist:
                    snd_min_dist = min_dist
                    snd_min_other = min_other
                    min_dist = magn
                    min_other = other
                elif magn < snd_min_dist:
                    snd_min_dist = magn
                    snd_min_other = other

                norm_x, norm_y = (other[0] - part[0])/magn, (other[1] - part[1])/magn,
                # factor = 1 / (1 + math.exp(-(len)))
                factor = 0.005 * (magn - 300)
                part[0] += factor * norm_x
                part[1] += factor * norm_y

            if min_other:
                min_dist_col = min(255, max(0, 600 - 7 * min_dist))
                pygame.draw.aaline(screen, (min_dist_col, min_dist_col, min_dist_col), (part[0], part[1]), (min_other[0], min_other[1]))
            if snd_min_other:
                snd_min_dist_col = min(255, max(0, 600 - 7 * snd_min_dist))
                pygame.draw.aaline(screen, (snd_min_dist_col, snd_min_dist_col, snd_min_dist_col), (part[0], part[1]), (snd_min_other[0], snd_min_other[1]))

            magn = math.hypot(x_m - part[0], y_m - part[1])
            norm_x, norm_y = (x_m - part[0])/magn, (y_m - part[1])/magn
            factor = 0.005 * (800 - magn)
            part[0] += factor * norm_x
            part[1] += factor * norm_y
            pygame.draw.circle(screen, (255, 255, 255), (part[0], part[1]), 4)

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.flip() 
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
