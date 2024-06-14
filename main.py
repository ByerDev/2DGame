from graphics import Graphics

print("A 2D space invaders game made by ByerDev. You'll begin by seeing the frame of the window. Adjust your terminal accordingly, then press enter. Press enter to show the frame.", end="")

input()

screen = Graphics(100)
input() # Wait for user to adjust terminal

screen.addSprite((25,25), "ship.png", "player") # Add player

i = 0
for y in range(6,44,5):
    for x in range(50,94,5):
        i += 1
        screen.addSprite((x,y), "enemy.png", "enemy_"+str(i))

screen.drawFrame()
input()

screen.endDraw()