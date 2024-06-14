from graphics import Graphics
import time
from pynput import keyboard

print("A 2D space invaders game made by ByerDev. You'll begin by seeing the frame of the window. Adjust your terminal accordingly, then press enter. After reading this message, press enter to go into the adjustment", end="")

screen = Graphics(100)

screen.addSprite([25,25], "ship.png", "player") # Add player

screen.endDraw()