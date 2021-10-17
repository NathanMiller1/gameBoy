import pgzrun
import random
import time

start_time = time.time()
seconds_to_run = 15
apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def hit_counter():
    hit_counter.apples_hit += 1

hit_counter.apples_hit = 0

def place_apple():
    apple.x = random.randint(10, 700)
    apple.y = random.randint(10, 500)

def on_mouse_down(pos):
    # Stop the game if time has elapsed
    if time.time() - start_time > seconds_to_run:
        print('You hit', hit_counter.apples_hit, 'apples.')
        quit()
    # If time has not elapsed check if the player hit the apple
    if apple.collidepoint(pos):
        hit_counter()
        print("Good Shot!")
        place_apple()
    else:
        print("Game Over. You hit", hit_counter.apples_hit, 'apples.')
        quit()

place_apple()

pgzrun.go()