#3.43
import math
def hit(centerX, centerY, radius, pointX, pointY):
    distance = math.sqrt((centerX - pointX)**2 + (centerY - pointY)**2)
    if (distance <= radius):
        print(True)
    else:
        print(False)