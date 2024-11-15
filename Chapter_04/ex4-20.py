from math import pi
from transforms import rotate_x_by

def transform_standard_basis(transform):
    '''
    3次元のベクトル変換を入力として取り、それを標準基底に適用した結果を出力する関数。
    この関数は、e_1, e_2, e_3 に座標変換を適用した結果を３つのベクトルのタプルで出力する
    '''
    vec_e1 = (1,0,0)
    vec_e2 = (0,1,0)
    vec_e3 = (0,0,1)

    return (transform(vec_e1), transform(vec_e2), transform(vec_e3))

print(transform_standard_basis(rotate_x_by(pi/2)))