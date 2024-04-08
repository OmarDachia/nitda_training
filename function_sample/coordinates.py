"""
Build a function to calculate the distance between two points on an x,y plane:
one with coordinates x1 and y1, and the other with coordinates x2 and y2.
Hint: You can use the following formula:

Use the coordinate distance calculator to find the distance between two coordinates in a two-dimensional or three-dimensional space. By simply entering the XY or XYZ coordinates of the points, this tool will instantly compute the distance between them!

Along with this tool, we've created a brief text where you'll find:

What the distance formula is for cartesian coordinates;
How to use this formula for determining the distance between coordinates in the 2D or 3D spaces; and
The distance formula for polar coordinates.

What is the distance formula for cartesian coordinates?
The general distance formula in cartesian coordinates is:

d = √[(x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²]

where:

d — Distance between two coordinates;
x₁, y₁ and z₁ — 3D coordinates of any of the points; and
x₂, y₂ and z₂— 3D coordinates of the other point.
This formula, which derives from the Pythagorean theorem, is also known as the Euclidian distance formula for three-dimensional space.

Although this formula includes the z coordinate, you may use it for both 2D and 3D spaces. By setting the z coordinates to zero, you can get a particular version for the distance between two points in a 2D space:

d = √[(x₂ - x₁)² + (y₂ - y₁)²]

Here d is the distance between two points in the two-dimensional space.

"""
import math

def cal_distance(x1,x2,y1,y2):
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))


print(cal_distance(float(input("Enter point for x1")),float(input("Enter point for x2")),float(input("Enter point for y1")),float(input("Enter point for y2"))))