import math
import sys
import os
from time import sleep
import cursor
from PIL import Image

class Graphics:
    """The class to draw stuff to the terminal window
    """
    def __init__(self, window_size: int) -> None:
        """__init__

        Args:
            window_size (int): The window width (aspect ratio stays at 2:1) of the game.
        """
        
        self.window_resolution = [window_size,math.floor(window_size/2)] # Set the actual resolution with a 2:1 Aspect Ratio (because I said so)
        
        self.pixelbuffer = []
        self.clearScreen()
        
        sys.stdout.write("test\n")
        cursor.hide()
        
        self.drawRow(0, True)
        self.drawRow(self.window_resolution[1]-1, True)
        self.drawColumn(0, True)
        self.drawColumn(self.window_resolution[0]-1, True)
        self.drawFrame()
        
    def clearScreen(self) -> None:
        """Clears the pixel buffer"""
        self.pixelbuffer = [[False for _ in range(self.window_resolution[0])][:] for _ in range(self.window_resolution[1])]
    def drawFrame(self, pixelbuffer:list[str] = None) -> None:
        """Draw the pixelbuffer to screen

        Args:
            pixelbuffer (list[str], optional): Optionally draw a self-made pixel buffer and save it internally. Defaults to None.
        """
        
        if pixelbuffer == None:
            usedPixelBuffer = self.pixelbuffer
        else:
            usedPixelBuffer = pixelbuffer
        
        
        out = []
        for l in range(len(usedPixelBuffer)):
            line = ""
            for p in range(self.window_resolution[0]):
                # Add a pixel to the line, if the value in the buffer is true, draw a square, otherwise don't. Then add a space to space the line out in accordance to the vertical space.
                if usedPixelBuffer[l][p]:
                    line += "■"
                else:
                    line += " "
                line += " "
            out.append(line)
        
        os.system("clear")
        sys.stdout.write("\n".join(out))
    
    def drawPixel(self, x: int, y: int, on: bool) -> None:
        """Draw a Pixel at the specified coordinates

        Args:
            x (int): x-coordinate
            y (int): y-coordinate
            on (bool): draw white (true) or black (false)
        """
        
        self.pixelbuffer[y][x] = on
    
    def drawRow(self, y: int, on: bool) -> None:
        """Draw an entire row at the same time

        Args:
            y (int): the y-position
            on (bool): draw white (true) or black (false)
        """
        
        self.pixelbuffer[y] = self.window_resolution[0]*[on]
    
    def drawColumn(self, x: int, on: bool) -> None:
        """Draw an entire row at the same time

        Args:
            x (int): the x-position
            on (bool): draw white (true) or black (false)
        """
        
        for y in range(len(self.pixelbuffer)):
            self.pixelbuffer[y][x] = on
            
    def drawSprite(self, sprite: Image.Image, x: int, y:int) -> None:
        """Draw a "sprite" to the specified position.

        Args:
            sprite (Image.Image): The sprite generated from Graphics.genSpriteFromImage
            x (int): x-position
            y (int): y-position
        """
        
        dim = sprite.size
        px = sprite.load()
        
        for cx in range(dim[1]):
            for cy in range(dim[0]):
                value = bool(round(sum(px[cx, cy])/3/256)) # Issue in here somewhere
                self.drawPixel(cx+(x-dim[0]/2),cy+(y-dim[1]/2), value)
    
    def endDraw(self) -> None:
        os.system("clear")
        cursor.show()
    
    
    def genSpriteFromImage(image_path: str) -> Image.Image:
        """Generate a Sprite from an Image

        Args:
            image_path (str): The path to the image

        Returns:
            Image.Image: 
        """
        
        im = Image.open(image_path)
        
        return im


if __name__ == "__main__":
    print("THIS IS ONLY FOR DEBUGGING PURPOSES")
    input()
    graphics = Graphics(100)
    sleep(1)
    testSprite = Graphics.genSpriteFromImage(sys.argv[1])
    graphics.drawSprite(testSprite, 0, 0)
    graphics.drawFrame()
    sleep(1)
    graphics.endDraw()