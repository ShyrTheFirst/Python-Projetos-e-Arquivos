import pygame
import sys
import random

PLAYER_TIME = 5 #seconds

def main():
    frames = pygame.time.Clock()
    print(pygame.time.Clock())
    input("That was pygame.time.Clock()")
    delta_time = 0
    player_timer = PLAYER_TIME
    random_timer = random.randint(1,10)
    actions_taken = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #handle actions with mouse clicks r keys
                #if click or key: actions_taken +=1
        player_timer -=delta_time #subtract time changed since last tick
        random_timer -=delta_time

        if player_timer <=0:
            print("Oops, tick tock. Times up!")
            player_timer = PLAYER_TIME #reset the timer
            
        if random_timer <= 0:
            print("Haha! Random event you get!")
            random_timer = random.randint(1,10)
            print("Player time: ", player_timer) #watch timer

        delta_time = frames.tick(60)/1000
        print(delta_time)
        input("that is delta time")
        print(frames.tick(60))
        input("that was frames.tick(60)")
        print(pygame.time.Clock())
        input("That was pygame.time.Clock()")


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((100,100))
    main()
