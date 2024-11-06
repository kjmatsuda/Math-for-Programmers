from math import sqrt, sin, cos, acos, atan2

def my_scale_2d(scalar, vector):
    x, y = vector
    return (scalar * x, scalar * y)

def my_scale_3d(scalar, vector):
    x, y, z = vector
    return (scalar * x, scalar * y, scalar * z)

# 本に記載の回答(Ex3.6)
def my_scale(scalar, vector):
    return tuple(scalar * coord for coord in vector)

def my_length(vector):
    return sqrt(sum(coord * coord for coord in vector))
