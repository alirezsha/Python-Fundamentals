class Point:
    """Representation of a point in two-dimensional space."""

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
    
class Rectangle:
    """Displaying a rectangle.
        attributes: Width, Height, Corner"""
rectangle1 = Rectangle()
rectangle1.width = 30.0
rectangle1.height = 60.0
rectangle1.corner = Point()
rectangle1.corner.x = 0.0
rectangle1.corner.y = 0.0

def center(rectangle):
    p = Point()
    p.x = rectangle.corner.x + rectangle.width/2
    p.y = rectangle.corner.y - rectangle.height/2
    return p
