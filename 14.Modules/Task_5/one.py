
import math

def area_circle(radius):
    return math.pi * radius**2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def perimeter_circle(radius):
    return 2 * math.pi * radius

def perimeter_rectangle(length, width):
    return 2 * (length + width)
