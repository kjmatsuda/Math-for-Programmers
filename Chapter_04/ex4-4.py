from teapot import load_triangles
from draw_model import draw_model
from vectors import scale, add
from transforms import polygon_map, compose

# 変換前のポット
# draw_model(load_triangles())

def scale2(v):
    return scale(2.0, v)

def translate1left(v):
    return add((-1,0,0), v)

# Ex4.4
# translate1leftとscale2を適用
# draw_model(polygon_map(compose(translate1left, scale2), load_triangles()))

# 次は逆の順で適用
draw_model(polygon_map(compose(scale2, translate1left), load_triangles()))
