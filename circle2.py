from cImage import *
import math
myImWin = ImageWin("Circle", 300, 300)
centerx = 150
centery = 150
radius = 100
circleImage = EmptyImage(300, 300)
for degrees in range(360):
    x = radius * math.cos(math.radians(degrees))
    y = radius * math.sin(math.radians(degrees))

    circleImage.setPixel(x + centerx, y + centery, Pixel(0, 0, 255))
    
circleImage.draw(myImWin)
myImWin.exitOnClick()

