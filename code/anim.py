#! /usr/bin/env python
# 3.7

import sys
import traceback            # traceback.print_stack(file=sys.stdout) to dump stack trace
import time

import matplotlib
import matplotlib.pyplot as plt     # diagnostics
from pprint import pprint


from numpy.random import randint
from pprint import pprint
import math

# REF: https://www.pygame.org/docs/ref/pygame.html
import pygame
pygame.init()          # initialize all imported pygame modules

PING_PONG_MASS = 0.0027 # 2.7g
PING_PONG_DIAM = 400    # 40mm

# simoulation environment variables - world_x,y,z
WORLD_SIZE_1 = 5000         # 500mm 10units / mmm
WORLD_X = WORLD_SIZE_1
WORLD_Y = WORLD_SIZE_1
WORLD_Z = WORLD_SIZE_1
wx, wy, wz = WORLD_X, WORLD_Y, WORLD_Z

window_size_X = 800 #640
window_size_Y = 600 #480

screen = pygame.display.set_mode((window_size_X,window_size_Y))
pygame.display.set_caption("Ping Pong Ball")

# Using: implementation of count sort & radix sort to test understanding
#

animation_timer = pygame.time.Clock()
# init position
x=WORLD_X * 0.5
y=WORLD_Y * 0.75
z=WORLD_Z * 0.5
# init speed
dx = 0 #75
dy = 0 #100
dz = 0 #200
# init accel
ddx = 0
ddy = 9
ddz = 0



def next_step(steps=1, time_in_ms=1):
    global x, y, z, dx, dy, dz
    
    for i in range(0,steps):
        x = x + dx 
        y = y + dy
        z = z + dz
        dx = dx + ddx 
        dy = dy + ddy
        dz = dz + ddz        
        if x > WORLD_X:
            x = WORLD_X
            dx *= -1
        if y > WORLD_Y:
            y = WORLD_Y
            dy = dy * -1
        if z > WORLD_Z:
            z = WORLD_Z
            dz = dz * -1
        if x < 0:
            x = 0
            dx *= -1
        if y < 0:
            y = 0
            dy = dy * -1
        if z < 0:
            z = 0
            dz = dz * -1
            
        print(f" x:{x},  y:{y},  z:{z}")
        print(f"dx:{dx}, dy:{dy}, dz:{dz}\n")
    

def draw_scaled_view(win, origin, x_size, y_size):
    global x, y, z, dx, dy, dz
    # quad - along x axis, y axis, z axis, from below
    #              BLHC,   BRHC,   TRHC,   ,TLHC
    
    scaled_x = int((x/WORLD_X) * x_size)
    scaled_y = int((y/WORLD_Y) * y_size)
    scaled_z = int((z/WORLD_Z) * 80) + 20 # 20px max away 100px closest
    ox, oy = origin
    
    pygame.draw.ellipse(win, (190,50,230), (ox+scaled_x,oy+scaled_y,scaled_z,scaled_z) )
    
    
def draw_window(win):
    global x, y, z, dx, dy, dz    

    win.fill((0,0,0))
            
    draw_scaled_view(win, (0,0), window_size_X, window_size_Y)    

    
def draw_iso(win):
    global x, y, z, dx, dy, dz    

    win.fill((0,0,0))
            
    # update_quadrant(TLHC)
    draw_scaled_view(win, (0,0), window_size_X/2, window_size_Y/2)    
    # update_quadrant(TRHC)
    draw_scaled_view(win, (window_size_X/2,0), window_size_X/2, window_size_Y/2)    
    # update_quadrant(BLHC)
    draw_scaled_view(win, (0,window_size_Y/2), window_size_X/2, window_size_Y/2)    
    # update_quadrant(BRHC)
    draw_scaled_view(win, (window_size_X/2,window_size_Y/2), window_size_X/2, window_size_Y/2)    
    

endLoop = False

dump=0
ticks = {}
start_time = time.time()
last_loop_start = 0
#frame_rates = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
#frame_rates = [2,4,6,8,10,20,30,40,50,60,70,80,90,100]
fr_reset = [10,20,30,40,-1]
frame_rates = list(fr_reset)
#frame_rates = [50,60,70,80,90,100]
#frame_rates = [10]
    # tick(), seconds per loop, FPS setting - animation_timer.tick(fps)
    # 0                 0.101    10
    # 0                 0.051    20
    # 0                 0.033    30
    # 0                 0.024    40
    # 0                 0.02     50
    # 0                 0.017    60  - hits loop over head @ ~60FPS ~ 17ms
    # 0                 0.017    70
    # 0                 0.018    80
    # 0                 0.016    90
    # 0                 0.016    100
sc_reset = [2,4,6,8,10,20,30,40,50,60,70,80,90,100]
sc_reset = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
sc_reset = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
step_calcs = list(sc_reset)
# FPS   steps loop_ms
# {10: [[100, 100],
#       [1000, 100],
#       [10000, 249],
#       [10000, 227],
#       [100000, 2137]]}



fps = frame_rates.pop(0)
steps = step_calcs.pop(0)

while not endLoop:
    # metrics
    loop_start = time.time() - start_time        
    if fps not in ticks: ticks[fps] = []
    ms_since_last_loop = round((loop_start - last_loop_start)*1000)
    ticks[fps].append( [ steps, ms_since_last_loop ] )    
    last_loop_start = loop_start
        
    # check events queue
    for e in pygame.event.get():
        print(e)
        
        if e.type == pygame.QUIT:
            endLoop = True
        
        if e.type == pygame.VIDEORESIZE:
            window_size_X = e.w
            window_size_Y = e.h
    
    # calculate / generate scene info
    #next_step(steps=10)
    next_step(ms_since_last_loop)
    
    # draw scene
    draw_window(screen)
    #draw_iso(screen)

    # limit to 30 FPS
    animation_timer.tick(10) # ~ a_timer.wait(100ms)

    # update display    
    pygame.display.update()

    # limit to 10 FPS
    #animation_timer.tick(10) # ~ a_timer.wait(100ms)

      

print(f"Exiting: {endLoop}")
print(f"pygame.TIMER_RESOLUTION: {pygame.TIMER_RESOLUTION}")
for fps in ticks:
    ticks[fps].pop(0)    # 1st value invalid





sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

# if __name__ == '__main__':
# 
#     
#     
#     
#     sys.exit(0)   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - EXIT < <

# FPS   steps  loop_time/ms
# {10: {500:  101,
#       1000: 100,
#       2000: 101,
#       3000: 101,
#       4000: 101,      OK - borderline between 4K-5K steps (calculation calls)
#       5000: 116,      Longer than frame rate = 100ms
#       6000: 139,
#       7000: 157,
#       8000: 168},
#  20: {500:  51,
#       1000: 50,
#       2000: 52,       OK - borderline between 2K-3K steps (calculation calls)
#       3000: 64,       Longer than frame rate = 500ms
#       4000: 84,
#       5000: 105,
#       6000: 126,
#       7000: 150,
#       8000: 167},
#  30: {500:  34,
#       1000: 34,       OK - borderline between 1K-2K steps (calculation calls)
#       2000: 44,       Longer than frame rate = 34ms
#       3000: 66,
#       4000: 86,
#       5000: 104,
#       6000: 125,
#       7000: 150,
#       8000: 195},
#  40: {500:  26,
#       1000: 26,       OK - borderline between 1K-2K steps (calculation calls)
#       2000: 43,       Longer than frame rate = 25ms
#       3000: 65,
#       4000: 86,
#       5000: 104,
#       6000: 124,
#       7000: 149,
#       8000: 170}}

