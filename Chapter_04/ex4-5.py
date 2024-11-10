from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map, compose, scale_by

# 変換前のポット
# draw_model(load_triangles())

# Ex4.5
# draw_model(polygon_map(compose(scale_by(0.4), scale_by(1.5)), load_triangles()))
# 以下と結果は同一になる
draw_model(polygon_map(scale_by(0.4 * 1.5), load_triangles()))
