#Write a Python program to calculate the area of regular polygon.
import math

num_sides = 4
side_length = 25

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

print("The area of the polygon is:", int(area))
