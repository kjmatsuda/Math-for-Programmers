from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map


# 変換前のポット
# draw_model(load_triangles())

# Ex4.9
def stretch_x(scalar, vector):
    x, y, z = vector
    return (scalar * x, y, z)

print(stretch_x(2, (2,3,4)))

def stretch_x_by(scalar):
    def new_function(v):
        return stretch_x(scalar, v)
    return new_function

print(stretch_x_by(2)((2,3,4)))

# draw_model(polygon_map(stretch_x(), load_triangles()))

