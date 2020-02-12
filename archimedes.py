import math

def archimedes(numSides, radius):
    innerAngleB = 360.0/ numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / (radius*2)
    return pi


 
