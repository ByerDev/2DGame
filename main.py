from graphics import Graphics

print("A 2D space invaders game made by ByerDev. You'll begin by seeing the frame of the window. Adjust your terminal accordingly, then press enter. Press enter to show the frame.", end="")

input()

screen = Graphics(100)

screen.addSprite((25,25), "ship.png", "player")

input() # Wait for user to adjust terminal

screen.drawFrame()
input()

screen.endDraw()