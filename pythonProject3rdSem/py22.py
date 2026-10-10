#Program to take radius of a circle from user and print it’s area and perimeter

import math
r=int(input("Enter the radius: "))
area=(math.pi*r**2)
perimeter=(2*math.pi*r)
print(f"The area is {area}")
print(f"The perimeter is {perimeter}")
