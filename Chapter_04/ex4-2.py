from teapot import load_triangles
from draw_model import draw_model
from vectors import add
from transforms import polygon_map

# 変換前のポット
# draw_model(load_triangles())

# Ex4.2
# Z軸の負の方向に20移動
def add_z_20(v):
    return add(v, (0,0,-20))
draw_model(polygon_map((add_z_20), load_triangles()))

