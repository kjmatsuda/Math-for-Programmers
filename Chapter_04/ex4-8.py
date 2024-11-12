from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map, compose, rotate_x_by, rotate_y_by, rotate_z_by
from math import pi

# 変換前のポット
# draw_model(load_triangles())

# Ex4.8
# draw_model(polygon_map(rotate_x_by(pi/2), load_triangles()))
draw_model(polygon_map(rotate_y_by(pi/2), load_triangles()))
# draw_model(polygon_map(rotate_z_by(pi/2), load_triangles()))

# draw_model(polygon_map(compose(rotate_z_by(pi/2), rotate_x_by(pi/2)), load_triangles()))
