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
        
        self.spriteBuffer: dict[dict[tuple[int]]] = {} # A buffer for displaying sprites. Format {filename:[spritename:(x1,y1), spritename:(x2,y2), ...]}
        
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

    def drawFrame(self, pixelbuffer:list[bool]|None = None, spritebuffer:dict[dict[tuple[int]]]|None = None) -> None:
        """Draw the pixelbuffer to screen

        Args:
            pixelbuffer (list[str], optional): Optionally draw a self-made pixel buffer and save it internally. Defaults to None.
        """
        
        if pixelbuffer == None:
            usedPixelBuffer = self.pixelbuffer
        else:
            usedPixelBuffer = pixelbuffer
        
        if spritebuffer == None:
            usedSpriteBuffer: dict[dict[tuple[int]]] = self.spriteBuffer
        else:
            usedSpriteBuffer: dict[dict[tuple[int]]] = spritebuffer
        
        
        for filename in usedSpriteBuffer.keys():
            for _,pos in usedSpriteBuffer[filename].items():
                self.drawSprite(Graphics.genSpriteFromImage("sprites/"+filename), pos)
        
        
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
            
    def drawSprite(self, sprite: Image.Image, pos: tuple[int]) -> None:
        """Draw a "sprite" to the specified position.

        Args:
            sprite (Image.Image): The sprite generated from Graphics.genSpriteFromImage
            pos (tuple[int]): The position of the sprite. The origin is the top left.
        """
        
        dim = sprite.size
        px = sprite.load()
        
        for cy in range(dim[1]):
            for cx in range(dim[0]):
                value = bool(round(sum(px[cx, cy])/3/256)) # Issue in here somewhere
                self.drawPixel(cx+pos[0], cy+pos[1], value) # If theres an error here, then thats because the image would go out of range of the screen
    
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
    
    def addSprite(self, pos: tuple, filename: str, name: str):
        """Add a sprite to the spritebuffer

        Args:
            pos (tuple): The position (x,y)
            filename (str): The filename of the RGB image
            name (str): The name of the sprite.
        """
        
        if not filename in self.spriteBuffer.keys():
            self.spriteBuffer[filename] = {}
        
        self.spriteBuffer[filename][name] = pos
            


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