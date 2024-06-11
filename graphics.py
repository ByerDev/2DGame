import math
import sys

nl = "\n" # Newline for use in f-Strings

class Graphics:
    """The class to draw stuff to the terminal window
    """
    def __init__(self, window_size: int):
        """__init__

        Args:
            window_size (int): The window width (aspect ratio stays at 2:1) of the game.
        """
        
        self.window_resolution = [window_size,math.floor(window_size/2)] # Set the actual resolution with a 2:1 Aspect Ratio (because I said so)
        
        self.pixelbuffer = []
        
        # screen borders
        self.pixelbuffer.append(self.window_resolution[0]*"■ ")
        self.pixelbuffer += ["■"+(self.window_resolution[0]-2)*"  "+" "+"■"]*(self.window_resolution[1]-2) # The inner part of the screen resolution display
        self.pixelbuffer.append(self.pixelbuffer[0])
        sys.stdout.write("\n".join(self.pixelbuffer))
    def clearScreen(self) -> None:
        """Clears the pixel buffer"""
        self.pixelbuffer = []

if __name__ == "__main__":
    graphics = Graphics(int(sys.argv[1]))