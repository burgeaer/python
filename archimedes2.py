import math

#def estimate_pi(length, n):
#    radius = float((length)/ (math.sqrt(2 - (2 *(math.cos((math.radians(360)/n)))))))
#    diameter = 2 * radius
#    circumference = (length * n)
#    return(float(circumference/diameter))
#print(str(estimate_pi(1, 5)))

diameter = float(input('Please Enter the Diameter of a circle: '))
area1 = (math.pi/4) * (diameter * diameter)
radius = diameter / 2
area2 = math.pi * radius * radius

print("Area of circle using direct formula = %.2f" %area1);
print("Area of circle using method 2 = %.2f" %area2)
