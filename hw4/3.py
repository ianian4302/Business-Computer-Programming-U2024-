import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = int(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print("The area of the circle is", area)