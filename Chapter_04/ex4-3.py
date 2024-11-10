from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map, scale_by

# 変換前のポット
# draw_model(load_triangles())

# Ex4.3
# ポットのベクトルを0と1の間の実数でscalar 倍してみる
# draw_model(polygon_map((scale_by(0.2)), load_triangles()))

# -1 倍してみる
draw_model(polygon_map((scale_by(-1)), load_triangles()))
