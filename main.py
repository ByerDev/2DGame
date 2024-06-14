from graphics import Graphics
import time
import threading
from operator import add

print("A 2D space invaders game made by ByerDev. You'll begin by seeing the frame of the window. Adjust your terminal accordingly, then press enter. After reading this message, press enter to go into the adjustment", end="")

#input()

screen = Graphics(100)
#input() # Wait for user to adjust terminal

screen.addSprite([50,40], "pixel.png", "player") # Add player
screen.addSprite([50,42], "paddle.png", "paddle")

vel: list[int] = [-1,-1]
pos: list[int] = [50,42]

framecounter = 0
running = True
try:
    while True:
        startTime: float = time.time()
        framecounter += 1
        if (pos[0] == 99 or not pos[0]):
            vel[0] *= -1
        if (pos[1] == 49 or not pos[1]):
            vel[1] *= -1
        pos = list(map(add, pos, vel))
        screen.editSprite("player", pos)
        screen.drawFrame()
        time.sleep(max(0,1/30-(time.time()-startTime)))
except KeyboardInterrupt:
    running = False

screen.endDraw()