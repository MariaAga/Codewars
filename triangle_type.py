# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    x,y,z = sorted([a,b,c])
    if (x+y)<=z:
        return 0
    if (x*x+y*y==z*z):
        return 2
    if z*z > (x*x + y*y):
        return 3
    return 1